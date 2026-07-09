"""
LeetCode 207 - Course Schedule
Approach 1: Topological Sort (BFS)
- Build the graph and track each course's indegree.
- Repeatedly take courses with indegree 0 and reduce the indegree of dependent courses.
- If all courses are processed, the schedule is possible.
Time: O(V + E)
Space: O(V + E)

Approach 2: DFS Cycle Detection
- Build the adjacency list and run DFS from every unvisited course.
- Use a recursion stack to detect back edges.
- If a cycle exists, the schedule is impossible.
Time: O(V + E)
Space: O(V + E)
"""

from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Indegree counts how many prerequisites each course has.
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        # Start with every course that has no prerequisites.
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Count how many courses can be completed in topological order.
        cnt = 0
        while queue:
            pre = queue.popleft()
            cnt += 1
            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return cnt == numCourses


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Build the directed graph of course dependencies.
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)

        # visited tracks processed nodes; recPath tracks the current DFS stack.
        visited = [0] * numCourses
        recPath = [0] * numCourses

        def dfs(pre):
            visited[pre] = 1
            recPath[pre] = 1

            for course in adj[pre]:
                if not visited[course]:
                    if not dfs(course):
                        return False
                elif recPath[course]:
                    return False

            recPath[pre] = 0
            return True

        # Run DFS from every course to catch cycles in disconnected graphs.
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True
