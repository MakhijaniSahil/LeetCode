# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
LeetCode 237 - Delete Node in a Linked List
Approach:
- Copy the value from the next node into the given node, then bypass
    the next node by adjusting pointers. This effectively 'deletes' the
    provided node without access to the list head.
Time: O(1)
Space: O(1)
"""


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy next node's value into current node.
        node.val = node.next.val
        # Skip over the next node to remove it from the list.
        node.next = node.next.next
