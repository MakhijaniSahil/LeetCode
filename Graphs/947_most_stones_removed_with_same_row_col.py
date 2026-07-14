"""
LeetCode 947 - Most Stones Removed with Same Row or Column
Approach:
- Treat each stone as a node in a graph.
- Connect two stones if they share a row or column.
- The maximum stones removed is the number of stones minus the number of connected components.
Time: O(n^2 * alpha(n))
Space: O(n)
"""


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # A single stone cannot be removed.
        n = len(stones)
        if n == 1:
            return 0

        # Union-find parent array.
        parent = [i for i in range(n)]

        # Find the root parent with path compression.
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        # Start with each stone as its own component.
        units = n
        for i in range(n):
            for j in range(i + 1, n):
                # Stones are connected if they share a row or a column.
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    pi, pj = find(i), find(j)
                    if pi != pj:
                        parent[pi] = pj
                        units -= 1

        return n - units
