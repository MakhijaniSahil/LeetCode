"""
LeetCode 1192 - Critical Connections in a Network
Approach:
- Run Tarjan's DFS to compute discovery times and low-link values.
- If a neighbor cannot reach an ancestor of the current node, the edge is a bridge.
- Collect every such bridge as a critical connection.
Time: O(n + e)
Space: O(n + e)
"""

from collections import defaultdict


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        # Build the undirected graph.
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # step[x] is the discovery time of node x.
        # low[x] is the earliest discovery time reachable from x.
        step = [0] * n
        low = [0] * n
        res = []

        # Mutable timer shared across recursive calls.
        time = [1]

        # DFS updates low-link values and detects bridges.
        def dfs(x, p):
            step[x] = low[x] = time[0]
            time[0] += 1

            for nei in adj[x]:
                if nei == p:
                    continue

                if not step[nei]:
                    dfs(nei, x)

                    low[x] = min(low[x], low[nei])

                    if low[nei] > step[x]:
                        res.append([x, nei])
                else:
                    low[x] = min(low[x], step[nei])

        # Handle disconnected graphs as well.
        for i in range(n):
            if not step[i]:
                dfs(i, -1)
        return res
