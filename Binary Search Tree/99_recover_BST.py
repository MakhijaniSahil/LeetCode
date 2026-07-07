"""
LeetCode 99 - Recover Binary Search Tree
Approach:
- Perform an inorder traversal to detect where the BST order breaks.
- The first inversion gives the first misplaced node and the middle node.
- A second inversion, if it exists, gives the last misplaced node.
- Swap the appropriate pair to restore the BST.
Time: O(n)
Space: O(h)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Track the nodes involved in the inorder order violation.
        self.prev = self.first = self.middle = self.last = None

        def inorder(node):
            if not node:
                return

            # Visit left subtree first to preserve inorder order.
            inorder(node.left)

            # A drop in value means the BST ordering is broken here.
            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                    self.middle = node
                else:
                    self.last = node

            self.prev = node

            # Then continue into the right subtree.
            inorder(node.right)

        inorder(root)

        # Swap the misplaced nodes back into their correct positions.
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val
