"""
LeetCode 802 - Find Eventual Safe States
Approach:
- Use DFS with three states: unvisited, safe, and unsafe.
- A node is safe if all paths starting from it eventually end at terminal nodes.
- Nodes that reach a cycle are marked unsafe.
Time: O(V + E)
Space: O(V)
"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # Number of nodes in the directed graph.
        n = len(graph)

        # safe: 0 = unvisited, 1 = safe, -1 = unsafe.
        # recPath marks nodes currently on the recursion stack.
        safe = [0] * n
        recPath = [0] * n

        # DFS returns True if the current node is eventually safe.
        def dfs(i):
            if safe[i] == 1:
                return True

            # Terminal nodes are immediately safe.
            if not graph[i]:
                safe[i] = 1
                return True

            # Revisiting a node on the current path means a cycle.
            if recPath[i] or safe[i] == -1:
                return False

            recPath[i] = 1

            # Every outgoing edge must lead to a safe node.
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    recPath[i] = 0
                    safe[i] = -1
                    return False

            safe[i] = 1
            recPath[i] = 0
            return True

        # Evaluate every node in case the graph has multiple components.
        for i in range(n):
            if safe[i] == 0:
                dfs(i)

        res = []

        # Collect the nodes marked safe in ascending order.
        for i, state in enumerate(safe):
            if state == 1:
                res.append(i)

        return res