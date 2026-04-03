# LeetCode 987 - Vertical Order Traversal of a Binary Tree
# Approach: BFS (track row/column coordinates)
# Time: O(n log n) due to sorting by column and row
# Space: O(n)

from collections import defaultdict
from queue import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Final result list to return.
        res = []
        # Hash map: column -> list of (row, value) pairs.
        map = defaultdict(list)
        # BFS queue: store [node, row, column] for each node.
        q = deque([[root, 0, 0]] if root else [])

        while q:
            # Dequeue node with its coordinates.
            node, row, col = q.popleft()

            # Create new column bucket if first time seeing this column.
            if col not in map:
                map[col] = []

            # Store (row, value) for later sorting by row within column.
            map[col].append((row, node.val))

            # Push child nodes with updated coordinates.
            if node.left:
                q.append([node.left, row + 1, col - 1])
            if node.right:
                q.append([node.right, row + 1, col + 1])

        # Join by columns in ascending order, then sort by row within each column.
        for col in sorted(map.keys()):
            level = sorted(map[col])
            # Extract values after sorting by row.
            res.append([val for row, val in level])
        return res
