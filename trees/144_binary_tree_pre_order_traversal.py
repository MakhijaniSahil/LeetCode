from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 144 - Binary Tree Preorder Traversal
Approach:
- Use an explicit stack to simulate recursive preorder traversal
- Visit node, then push right child, then left child so left is processed first
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        # Stack keeps the next nodes to visit in preorder.
        stack = deque([root])
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push right first so left is popped and processed next.
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
