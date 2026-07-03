from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 199 - Binary Tree Right Side View
Approach:
- Run level-order traversal (BFS)
- At each level, take the last node visited as the visible right-side node
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        result = []
        queue = deque([root])

        # Process one level at a time.
        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                # The last node in this level is the rightmost visible node.
                if i == n - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
