# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
LeetCode 160 - Intersection of Two Linked Lists
Approach:
- Use two pointers that traverse both lists
- When one pointer reaches the end, redirect it to the other list's head
- If the lists intersect, the pointers meet at the shared node
Time: O(m + n)
Space: O(1)
"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        a, b = headA, headB

        # After at most two passes, both pointers align on the intersection
        # node or on None if the lists do not intersect.
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
