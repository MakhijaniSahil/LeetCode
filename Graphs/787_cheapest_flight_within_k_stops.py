"""
LeetCode 787 - Cheapest Flights Within K Stops
Approach 1: Priority Queue Search
- Build an adjacency list of flight costs.
- Use a min-heap to always expand the cheapest reachable state first.
- Track the best fare for each `(node, stops)` pair to avoid reprocessing worse states.
Time: O(E log E)
Space: O(E)

Approach 2: Bellman-Ford Relaxation
- Repeatedly relax all edges for `k + 1` rounds.
- Each round uses a copy of the previous distances so only paths with at most that many stops are considered.
Time: O(k * E)
Space: O(n)
"""

from collections import defaultdict
import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Build adjacency list keyed by source city.
        adj = defaultdict(list)
        for s, d, price in flights:
            adj[s].append([d, price])

        # Heap stores [current fare, stops used, current city].
        heap = [[0, -1, src]]
        dist = {(src, -1): 0}

        while heap:
            fare, stops, curr = heapq.heappop(heap)

            # The first time we pop the destination, it is the cheapest valid route.
            if curr == dst:
                return fare

            # Stop expanding once we have used all allowed stops.
            if stops == k:
                continue

            for d, price in adj[curr]:
                updatedFare = fare + price

                # Keep only the best fare seen for this city with this stop count.
                if updatedFare < dist.get((d, stops + 1), float('inf')):
                    dist[(d, stops + 1)] = updatedFare
                    heapq.heappush(heap, [updatedFare, stops + 1, d])

        return -1


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # prices[i] stores the cheapest known cost to reach city i.
        prices = [float('inf')] * n

        prices[src] = 0

        # Relax all flights up to k + 1 times.
        for _ in range(k+1):
            temp = prices[:]
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue

                # Update the next round if this edge gives a cheaper route.
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p

            prices = temp

        return prices[dst] if prices[dst] != float('inf') else -1
