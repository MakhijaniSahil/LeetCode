"""
LeetCode 743 - Network Delay Time
Approach:
- Build a directed weighted graph from the travel times.
- Run Dijkstra's algorithm from the source node.
- The answer is the maximum shortest-path time among all nodes, or -1 if any node is unreachable.
Time: O(E log V)
Space: O(V + E)
"""

from collections import defaultdict
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # Build adjacency list using 0-based node indices.
        adj = defaultdict(list)
        for s, d, w in times:
            adj[s - 1].append((d - 1, w))

        # Dijkstra state: (current time, node).
        heap = [(0, k - 1)]
        time = [float('inf')] * n
        time[k - 1] = 0

        # Expand the currently known fastest node each round.
        while heap:
            t, s = heapq.heappop(heap)

            if t > time[s]:
                continue

            for d, w in adj[s]:
                # Relax the edge if it improves the known travel time.
                if t + w < time[d]:
                    time[d] = t + w
                    heapq.heappush(heap, (time[d], d))

        if float('inf') in time:
            return -1
        else:
            return max(time)
