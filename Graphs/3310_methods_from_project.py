"""
LeetCode 3310 - Remaining Methods
Approach 1: DFS from the Suspicious Method
- Build the invocation graph.
- Start from method k and mark every reachable method as suspicious.
- If any non-suspicious method invokes a suspicious one, the answer is all methods.
Time: O(n + e)
Space: O(n + e)

Approach 2: BFS with Indegree Tracking
- Build the invocation graph and indegree array.
- Start from method k and mark all reachable methods as suspicious.
- If a suspicious method still has incoming edges from safe methods, the answer is all methods.
Time: O(n + e)
Space: O(n + e)
"""

from collections import defaultdict
from collections import deque


class Solution(object):
    def remainingMethods(self, n, k, invocations):  # My own Soln
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Build the directed invocation graph.
        adj = defaultdict(list)

        for u, v in invocations:
            adj[u].append(v)

        # Track all methods reachable from k.
        visited = set()
        suspicious = set()

        # Mark every method in k's dependency chain as suspicious.
        def rec(u):
            if u in visited:
                return

            visited.add(u)
            suspicious.add(u)

            for v in adj[u]:
                rec(v)

        rec(k)

        # If every method is suspicious, none can be removed safely.
        cnt = len(suspicious)
        if cnt == n:
            return []

        res = []

        # Any safe method that invokes a suspicious one invalidates the pruning.
        for i in range(n):
            if i in suspicious:
                continue
            for j in adj[i]:
                if j in suspicious:
                    return [x for x in range(n)]
            res.append(i)

        return res


class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Build the graph and indegree counts.
        adj = defaultdict(list)
        inDegree = [0] * n
        suspicious = [False] * n
        for u, v in invocations:
            adj[u].append(v)
            inDegree[v] += 1

        # BFS from k to mark all suspicious methods.
        q = deque([k])
        suspicious[k] = True
        while q:
            curr = q.popleft()

            for nei in adj[curr]:
                inDegree[nei] -= 1
                if not suspicious[nei]:
                    q.append(nei)
                    suspicious[nei] = True

        res = []

        # If a suspicious method still has incoming edges from safe methods, remove nothing.
        for i in range(n):
            if suspicious[i] and inDegree[i] > 0:
                return [x for x in range(n)]

            if not suspicious[i]:
                res.append(i)

        return res
