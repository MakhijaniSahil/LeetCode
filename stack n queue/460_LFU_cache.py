"""
LeetCode 460 - LFU Cache
Approach:
- Use two hash maps: one mapping keys to values/frequencies, and another mapping frequencies to doubly linked lists of keys.
- The first map gives O(1) access to update node values and counts.
- The second map groups keys by frequency, and the doubly linked list maintains the LRU order among keys with the same frequency.
- A variable tracks the minimum frequency (lfuCnt) to quickly find the list from which to evict when capacity is reached.
Time: O(1) for get and put
Space: O(capacity)
"""

from collections import defaultdict

class Node:
    def __init__(self, value , prev = None, next = None):
        # Initialize a node with value and pointers.
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        # Dummy nodes for boundaries of the doubly linked list.
        self.left = Node(0)
        self.right = Node(0 , self.left)
        self.left.next = self.right
        # Map stores values to nodes for O(1) access.
        self.map = {}
        
    def length(self):
        # Return the number of elements in the list.
        return len(self.map)
    
    def pushRight(self, value):
        # Insert a new node right before the right dummy node (most recently used).
        node = Node(value , self.right.prev , self.right)
        self.right.prev.next = node
        self.right.prev = node
        self.map[value] = node
    
    def pop(self,value):
        # Remove a node by its value if it exists in the list.
        if value in self.map:
            node = self.map[value]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.map[value]
    
    def popLeft(self):
        # Remove and return the least recently used node (next to left dummy).
        node = self.left.next
        self.pop(node.value)
        return node.value
    
    def update(self, value):
        # Move an accessed node to the most recently used position.
        self.pop(value)
        self.pushRight(value)

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # lfuCnt tracks the minimum frequency of all elements.
        self.lfuCnt = 0
        # valueMap stores the key-value pairs.
        self.valueMap = {}
        # countMap stores the frequency count for each key.
        self.countMap = defaultdict(int)
        # listMap maps frequencies to their corresponding doubly linked lists.
        self.listMap = defaultdict(LinkedList)

    def counter(self,key):
        # Increment frequency and move the key to the next frequency list.
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)
        
        # Update lfuCnt if the minimum frequency list becomes empty.
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Return -1 if key is not found.
        if key not in self.valueMap:
            return -1
        # Update frequency and return the value.
        self.counter(key)
        return self.valueMap[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Return if capacity is 0 as nothing can be inserted.
        if self.capacity == 0:
            return
        
        # Evict the least recently used key from the minimum frequency list if at capacity.
        if key not in self.valueMap and len(self.valueMap)==self.capacity:
            res = self.listMap[self.lfuCnt].popLeft()
            self.valueMap.pop(res)
            self.countMap.pop(res)
        
        # Update value, increment its frequency, and update lfuCnt.
        self.valueMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])