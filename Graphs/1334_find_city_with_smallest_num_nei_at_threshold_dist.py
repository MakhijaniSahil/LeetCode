"""
LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
Approach:
- Build an undirected weighted graph.
- Run Dijkstra's algorithm from each city to count how many cities are reachable within the threshold.
- Pick the city with the smallest count, breaking ties by choosing the larger city index.
Time: O(n * (E log V))
Space: O(V + E)
"""

from collections import defaultdict
import heapq


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # Build an undirected adjacency list.
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((d, w))
            adj[d].append((s, w))

        # Shared heap and distance array reused for each source city.
        minHeap = []
        dist = [float('inf')] * n

        # Dijkstra run from the current origin city.
        def djikstra(origin):
            while minHeap:
                d, u = heapq.heappop(minHeap)

                if d > dist[u]:
                    continue

                for v, w in adj[u]:
                    newDist = d + w

                    # Only keep improvements that stay within the threshold.
                    if newDist < dist[v] and newDist <= distanceThreshold:
                        dist[v] = newDist
                        heapq.heappush(minHeap, (newDist, v))

        minLen = float('inf')
        minCity = -1

        # Evaluate every city as a possible answer.
        for i in range(n):
            minHeap = [(0,i)]
            dist = [float('inf')] * n
            dist[i] = 0
            djikstra(i)

            count = 0
            for d in dist:
                if d <= distanceThreshold:
                    count += 1
            count -= 1

            # Keep the city with the smallest count; larger index wins ties.
            if count <= minLen:
                minLen = count
                minCity = i

        return minCity
