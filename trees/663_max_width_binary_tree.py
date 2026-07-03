from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 662 - Maximum Width of Binary Tree
Approach:
- Level-order traversal with positional indices as if the tree were complete
- Width at each level is rightmost_index - leftmost_index + 1
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        # Store pairs of (node, virtual_index).
        queue = deque([(root, 1)])
        max_width = 1

        while queue:
            n = len(queue)
            left = queue[0][1]
            right = queue[-1][1]
            max_width = max(max_width, right - left + 1)

            for _ in range(n):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))

        return max_width
