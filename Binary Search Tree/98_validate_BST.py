# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
LeetCode 98 - Validate Binary Search Tree
Approach:
- Recursively enforce valid value ranges for each subtree using min/max bounds.
- For left child, upper bound becomes parent.val - 1; for right, lower bound becomes parent.val + 1.
- This ensures all nodes satisfy BST ordering, not just immediate children.
Time: O(n)
Space: O(h) recursion stack
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Use 32-bit int bounds as initial range (works for typical LeetCode inputs).
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        def is_valid(node, min_val, max_val):
            # An empty subtree is valid.
            if not node:
                return True

            # Current node must lie within (min_val, max_val) inclusive.
            if not (min_val <= node.val <= max_val):
                return False

            # Recurse: left subtree values must be < node.val, right subtree values must be > node.val.
            # We use node.val-1 and node.val+1 to keep integer bounds consistent with equality checks.
            return is_valid(node.left, min_val, node.val - 1) and is_valid(
                node.right, node.val + 1, max_val
            )

        return is_valid(root, INT_MIN, INT_MAX)
