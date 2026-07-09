"""
LeetCode 210 - Course Schedule II
Approach:
- Build the prerequisite graph and track indegrees for every course.
- Use topological sorting to remove courses with indegree 0 first.
- If we process all courses, the resulting order is valid; otherwise return an empty list.
Time: O(V + E)
Space: O(V + E)
"""

from collections import deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list and indegree count.
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        # Start with all courses that have no prerequisites.
        queue = deque()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)

        # Collect courses in topological order.
        res = []
        while queue:
            pre = queue.popleft()
            res.append(pre)

            for course in adj[pre]:
                indegree[course] -= 1
                if not indegree[course]:
                    queue.append(course)

        # If not all courses were processed, a cycle exists.
        if len(res) != numCourses:
            return []
        return res
