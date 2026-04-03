# LeetCode 104 - Maximum Depth of Binary Tree
# Approach: Recursion
# Time: O(n)
# Space: O(h)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Empty subtree has depth 0.
        if not root:
            return 0

        # Compute depth of left and right subtrees.
        left = root.left
        right = root.right

        # Current node adds 1 to the deeper subtree.
        return 1 + max(self.maxDepth(left), self.maxDepth(right))
