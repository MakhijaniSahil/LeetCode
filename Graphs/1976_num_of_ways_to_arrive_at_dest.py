"""
LeetCode 1976 - Number of Ways to Arrive at Destination
Approach:
- Use Dijkstra's algorithm to find the shortest distance to each node.
- Track how many shortest paths lead to each node while relaxing edges.
- If a new path matches the best known distance, add its count to the total.
Time: O(E log V)
Space: O(V + E)
"""

from collections import defaultdict
import heapq


class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Build an undirected weighted graph.
        adj = defaultdict(list)
        for s, d, w in roads:
            adj[s].append((d, w))
            adj[d].append((s, w))

        MOD = 10**9 + 7

        # Min-heap of (current cost, node).
        minHeap = [(0, 0)]
        minCost = [float('inf')] * n
        minCost[0] = 0

        # pathCount[i] stores the number of shortest paths to node i.
        pathCount = [0]*n
        pathCount[0] = 1

        # Standard Dijkstra traversal with path counting.
        while minHeap:
            cost, u = heapq.heappop(minHeap)

            if cost > minCost[u]:
                continue

            for v, w in adj[u]:
                newCost = cost + w

                # Found a strictly better route to v.
                if newCost < minCost[v]:
                    minCost[v] = newCost
                    pathCount[v] = pathCount[u]
                    heapq.heappush(minHeap, (newCost, v))
                # Found another shortest route to v.
                elif newCost == minCost[v]:
                    pathCount[v] = (pathCount[v] + pathCount[u]) % MOD

        return pathCount[n-1]
