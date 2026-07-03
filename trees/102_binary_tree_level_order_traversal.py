from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 102 - Binary Tree Level Order Traversal
Approach:
- Use a queue to process nodes level by level
- For each level, record all node values before moving to the next level
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        result = []
        queue = deque([root])

        # Process one full tree level at a time.
        while queue:
            n = len(queue)
            level = []

            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)

                # Enqueue children for the next level.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
