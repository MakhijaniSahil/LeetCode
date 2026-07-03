# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
LeetCode 236 - Lowest Common Ancestor of a Binary Tree
Approach:
- Recurse into left and right subtrees
- If both sides find one of the targets, current node is the LCA
- If only one side returns a node, propagate it upward
Time: O(n)
Space: O(h) recursion stack
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Stop when we hit the end or one of the target nodes.
        if not root or root == p or root == q:
            return root

        # Search both subtrees for the target nodes.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides found a target, current node is the split point.
        if left and right:
            return root

        # Otherwise return whichever side found a target.
        return left if left else right
