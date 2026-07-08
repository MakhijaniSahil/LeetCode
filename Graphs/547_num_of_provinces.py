"""
LeetCode 547 - Number of Provinces
Approach 1: Depth-First Search
- Start a DFS from every unvisited city.
- Mark all cities reachable from that start as part of the same province.
Time: O(n^2)
Space: O(n)

Approach 2: Union Find
- Treat each city as its own set initially.
- Union any pair of directly connected cities.
- The remaining number of sets is the number of provinces.
Time: O(n^2)
Space: O(n)
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of cities and visited markers for DFS traversal.
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        # Visit every city reachable from the current starting city.
        def dfs(e):
            for v in range(n):
                if isConnected[e][v] == 1 and not visited[v]:
                    visited[v] = True
                    dfs(v)

        # Launch a new DFS whenever we find an unseen city.
        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i)
        return provinces


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Start with each city in its own province.
        n = len(isConnected)
        provinces = n
        parent = [i for i in range(n)]
        rank = [1] * n

        # Find the representative for a set with path compression.
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        # Merge two sets if they are currently disconnected.
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x == parent_y:
                return False

            if rank[parent_x] > rank[parent_y]:
                parent[parent_y] = parent_x
            elif rank[parent_x] < rank[parent_y]:
                parent[parent_x] = parent_y
            else:
                parent[parent_y] = parent_x
                rank[parent_x] += 1

            return True

        # Only inspect the upper triangle of the matrix to avoid duplicate edges.
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and union(i, j):
                    provinces -= 1

        return provinces
