"""
LeetCode 84 - Largest Rectangle in Histogram
Approach:
- Use a monotonic increasing stack of `(start_index, height)` pairs.
- When a shorter bar appears, pop taller bars and compute the largest area they can form.
- After the scan, process the remaining bars as extending to the end of the histogram.
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
        # Increasing stack of bars waiting for their right boundary.
        stack = deque()
        max_area = 0

        i = 0

        # Expand through the histogram and resolve rectangles when height drops.
        while i < len(heights):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                # Count how far the new shorter bar can extend to the left.
                cnt = 0
                while stack and heights[i] < stack[-1][1]:
                    w, h = stack.pop()
                    cnt += 1
                    area = (i - w) * h
                    max_area = max(max_area, area)

                # Reuse the earliest valid start index for the shorter bar.
                stack.append((i - cnt, heights[i]))

            i += 1

        # Remaining bars extend to the end of the histogram.
        while stack:
            w, h = stack.pop()
            area = (len(heights) - w) * h
            max_area = max(max_area, area)

        return max_area
