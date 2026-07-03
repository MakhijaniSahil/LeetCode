from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 145 - Binary Tree Postorder Traversal
Approaches:
- Iterative postorder using a stack and a previous-node pointer
- Reverse preorder trick: visit root-right-left, then reverse the result
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        # Keep track of the last node we visited so we know whether to
        # traverse a right subtree or finish the current node.
        stack = deque()
        prev = None
        result = []

        # Walk down the left spine, then decide whether to go right or visit.
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            top = stack[-1]
            if top.right and prev != top.right:
                root = top.right
            else:
                result.append(top.val)
                prev = stack.pop()

        return result


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        # Reverse preorder variant: collect nodes in root-right-left order,
        # then reverse the list to obtain left-right-root postorder.
        stack = deque([root])
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first so the right child is processed before it.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]
