"""
LeetCode 785 - Is Graph Bipartite?
Approach:
- Use DFS to color the graph with two colors.
- Adjacent nodes must always end up in opposite sets.
- If we ever see a conflict, the graph is not bipartite.
Time: O(V + E)
Space: O(V)
"""


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # Two sets represent the two sides of the bipartition.
        setA = set()
        setB = set()
        n = len(graph)

        # Track which nodes have already been colored.
        visited = [0] * n

        # DFS assigns the current node to one side and checks neighbors.
        def dfs(u, s):
            visited[u] = 1
            setA.add(u) if not s else setB.add(u)

            for v in graph[u]:
                if visited[v]:
                    if s and v in setB:
                        return False
                    elif not s and v in setA:
                        return False
                else:
                    if not dfs(v, not s):
                        return False

            return True

        # Start a new DFS from every disconnected component.
        for i in range(n):
            if not visited[i]:
                if not dfs(i, False):
                    return False
        return True
