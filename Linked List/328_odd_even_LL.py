# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
LeetCode 328 - Odd Even Linked List
Approach:
- Maintain two chains: one for odd-indexed nodes and one for even-indexed nodes
- Rewire pointers in-place, then append the even list after the odd list
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # `odd` walks the odd-positioned nodes, `even` walks the even ones.
        odd = head
        even = head.next
        even_head = even

        # Stitch odd nodes together, then even nodes together.
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # Attach the even list after the odd list.
        odd.next = even_head
        return head