"""
LeetCode 84 - Largest Rectangle in Histogram
Approach:
- Maintain a monotonic increasing stack of `(start_index, height)` pairs.
- When a shorter bar appears, pop taller bars and compute the best rectangle for each.
- After the scan, treat the remaining bars as extending to the end of the histogram.
Time: O(n)
Space: O(n)
"""

from collections import deque


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Stack stores bars waiting for a smaller height on the right.
        stack = deque()
        max_area = 0

        i = 0

        # Scan each bar and resolve taller bars when the height drops.
        while i < len(heights):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                # Carry the earliest start index across all popped taller bars.
                start = 0
                while stack and heights[i] < stack[-1][1]:
                    w, h = stack.pop()
                    start = w
                    area = (i - w) * h
                    max_area = max(max_area, area)

                # The current shorter bar can begin where the last taller bar began.
                stack.append((start, heights[i]))

            i += 1

        # Any bars left in the stack extend to the end of the array.
        while stack:
            w, h = stack.pop()
            area = (len(heights) - w) * h
            max_area = max(max_area, area)

        return max_area
