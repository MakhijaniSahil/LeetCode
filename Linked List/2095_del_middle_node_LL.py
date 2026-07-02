# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
LeetCode 2095 - Delete the Middle Node of a Linked List
Approach:
- Use slow/fast pointers to find the middle node
- Keep track of the node before slow so we can bypass the middle node
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        # Move fast twice as fast as slow so slow lands on the middle node.
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Skip the middle node by linking its predecessor to its successor.
        prev.next = slow.next
        return head
