from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 94 - Binary Tree Inorder Traversal
Approach:
- Use an explicit stack to simulate recursive inorder traversal
- Walk left as far as possible, visit the node, then move right
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        # Stack stores the path to the current node's ancestors.
        stack = deque()
        result = []

        # Traverse left, then visit, then traverse right.
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result
