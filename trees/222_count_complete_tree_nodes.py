# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 222 - Count Complete Tree Nodes
Approach:
- If left and right depths are equal, the tree is perfect: return 2^depth - 1
- Otherwise, one subtree is perfect and the other is not; recurse accordingly
Time: O((log n)^2)
Space: O(log n) recursion stack
"""

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        # Count depth by traversing right edge.
        right_depth = 0
        right = root
        while right:
            right_depth += 1
            right = right.right

        # Count depth by traversing left edge.
        left_depth = 0
        left = root
        while left:
            left_depth += 1
            left = left.left

        # If depths are equal, tree rooted at `root` is a perfect binary tree.
        if right_depth == left_depth:
            return 2**right_depth - 1
        else:
            # Otherwise recurse on left and right subtrees.
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
