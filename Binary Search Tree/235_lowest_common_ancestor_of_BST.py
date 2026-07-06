# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree
Approach:
- Use BST ordering to find split point where p and q diverge.
- If both targets are less than current node, go left; if both greater, go right.
- Otherwise current node is the lowest common ancestor (split point).
Time: O(h) where h is tree height
Space: O(1)
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Guard: empty tree or if root equals one of the targets.
        if not root or root == p or root == q:
            return root

        # Iteratively walk down the tree using BST properties.
        while root:
            # Both targets in left subtree.
            if p.val < root.val and q.val < root.val:
                root = root.left

            # Both targets in right subtree.
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # Targets are on different sides, or one equals the root: split point found.
            else:
                return root
