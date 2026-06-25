"""
LeetCode 146 - LRU Cache
Approach:
- Combine a hash map with a doubly linked list.
- The hash map gives O(1) access to cache nodes by key.
- The linked list keeps usage order, with the least recently used node near the left dummy
  and the most recently used node near the right dummy.
Time: O(1) for get and put
Space: O(capacity)
"""


class Node:
    def __init__(self, key, value):
        # Store both key and value so eviction can remove the map entry too.
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # Cache maps keys to nodes in the linked list.
        self.capacity = capacity
        self.cache = {}

        # Dummy boundary nodes simplify insert and remove operations.
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Disconnect a node from its current position.
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # Insert node right before the right dummy as most recently used.
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Move accessed key to the most recently used position.
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Remove existing node so the updated value can be reinserted as most recent.
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Evict the least recently used node when capacity is exceeded.
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
