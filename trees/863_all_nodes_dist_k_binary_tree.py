from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
LeetCode 863 - All Nodes Distance K in Binary Tree
Approach:
- Build a parent map so we can traverse upward from any node
- BFS from the target node, treating the tree as an undirected graph
- Collect all nodes exactly k steps away
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        # Map each node to its parent so we can traverse upward.
        parent = {}

        # BFS to build the parent map.
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node.left:
                parent[node.left] = node
                queue.append(node.left)

            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        res = []

        # BFS from target node, treating tree as undirected graph.
        def bfs(res, k):
            visited = {target}
            queue = deque([target])
            while queue and k > 0:
                n = len(queue)
                while n > 0:
                    n -= 1
                    curr = queue.popleft()

                    # Traverse left child if not visited.
                    if curr.left and curr.left not in visited:
                        visited.add(curr.left)
                        queue.append(curr.left)

                    # Traverse right child if not visited.
                    if curr.right and curr.right not in visited:
                        visited.add(curr.right)
                        queue.append(curr.right)

                    # Traverse parent if not visited.
                    if curr in parent and parent[curr] not in visited:
                        visited.add(parent[curr])
                        queue.append(parent[curr])

                k -= 1

            # Collect all nodes at exactly distance k.
            while queue:
                res.append(queue.popleft().val)

        bfs(res, k)
        return res