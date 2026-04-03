# LeetCode 103 - Binary Tree Zigzag Level Order Traversal
# Approach 1: DFS (track level and insert by parity)
# Time: O(n^2) in worst case due to front inserts
# Approach 2: BFS (level order traversal)
# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
from collections import deque


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Stores zigzag order values level by level.
        res = []

        def dfs(root, level):
            # Base case: no node to process.
            if not root:
                return

            # Create a new bucket when we reach a new depth.
            if len(res) <= level:
                res.append([])

            # Even levels append normally, odd levels insert at front.
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)

            # Traverse children with next depth.
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        # Start DFS from root at level 0.
        dfs(root, 0)
        return res


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Stores final zigzag traversal.
        res = []

        # Initialize queue with root if tree is non-empty.
        q = deque([root] if root else [])

        # Standard BFS traversal by levels.
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                # Push next level nodes.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Reverse every alternate level to maintain zigzag order.
            level = reversed(level) if len(res) % 2 else level
            res.append(level)

        return res
