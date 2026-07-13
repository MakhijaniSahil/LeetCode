"""
LeetCode 1319 - Number of Operations to Make Network Connected
Approach 1: Depth-First Search
- If there are fewer than `n - 1` cables, connecting the network is impossible.
- Otherwise, count the number of connected components with DFS.
- The answer is the number of components minus one.
Time: O(n + e)
Space: O(n + e)

Approach 2: Union Find
- If there are fewer than `n - 1` cables, connecting the network is impossible.
- Union all directly connected computers.
- The answer is the number of remaining components minus one.
Time: O(n + e)
Space: O(n)
"""

from collections import defaultdict


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # At least n - 1 cables are required to connect n computers.
        if len(connections) < n - 1:
            return -1

        # Build the undirected graph of connections.
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Count how many connected components exist.
        units = 0
        visited = [0] * n

        # Mark every computer reachable from the current start node.
        def dfs(u):
            visited[u] = 1

            for v in adj[u]:
                if not visited[v]:
                    dfs(v)

        # Each unvisited node starts a new component.
        for i in range(n):
            if not visited[i]:
                units += 1
                dfs(i)

        return units - 1


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # At least n - 1 cables are required to connect n computers.
        if len(connections) < n - 1:
            return -1

        # Parent array for union-find.
        parent = [i for i in range(n)]

        # Find the root parent with path compression.
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        # Start with each computer as its own component.
        units = n
        for u, v in connections:
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                units -= 1

        return units - 1
