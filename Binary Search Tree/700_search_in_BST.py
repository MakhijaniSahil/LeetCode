# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
LeetCode 700 - Search in a Binary Search Tree
Approach:
- Use BST property: left subtree < node < right subtree.
- Recurse towards the side that could contain `val` until found or null.
Time: O(h) where h is tree height
Space: O(h) recursion stack (or O(1) iterative)
"""


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # Guard: empty tree.
        if not root:
            return None

        # If current node matches, return it.
        if root.val == val:
            return root

        # If target is smaller, it must be in left subtree (if exists).
        if root.val > val:
            return self.searchBST(root.left, val) if root.left else None

        # If target is larger, it must be in right subtree (if exists).
        return self.searchBST(root.right, val) if root.right else None
