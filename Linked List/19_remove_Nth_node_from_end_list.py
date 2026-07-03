# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
LeetCode 19 - Remove Nth Node From End of List
Approach:
- Use a dummy node so removing the head is handled uniformly
- Move `fast` n steps ahead, then advance `fast` and `slow` together
  until `fast` reaches the last node
- `slow.next` is the node to remove
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Dummy node simplifies deleting the first real node when needed.
        temp = ListNode(0)
        temp.next = head
        fast = temp
        slow = temp

        # Advance fast pointer n steps ahead.
        for _ in range(n):
            if fast:
                fast = fast.next

        # Move both pointers until fast is at the tail.
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Bypass the target node.
        slow.next = slow.next.next
        return temp.next
