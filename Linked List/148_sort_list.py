# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
LeetCode 148 - Sort List
Approach:
- Use merge sort on the linked list
- Find the middle with slow/fast pointers, split the list, sort both halves,
  and merge the sorted halves
Time: O(n log n)
Space: O(log n) recursion stack
"""


class Solution(object):
    def getMid(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Slow advances one step and fast advances two; slow ends at the node
        # just before the start of the right half.
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, l, r):
        # Dummy node simplifies building the merged sorted list.
        head = tail = ListNode()

        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next

        if l:
            tail.next = l
        if r:
            tail.next = r
        return head.next

    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # Split the list into two halves.
        l = head
        r = self.getMid(head)
        temp = r.next
        r.next = None
        r = temp

        # Recursively sort each half, then merge the two sorted lists.
        l = self.sortList(l)
        r = self.sortList(r)
        return self.merge(l, r)
