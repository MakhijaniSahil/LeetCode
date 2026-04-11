# LeetCode 435 - Non-overlapping Intervals
# Approach: Greedy (keep interval with smaller end on overlap)
# Time: O(n log n)
# Space: O(1)


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort intervals by start time.
        intervals.sort()
        # Count intervals removed due to overlap.
        count = 0
        # Track the last interval kept in the non-overlapping set.
        prev = intervals[0]

        for i in range(1, len(intervals)):
            # No overlap: keep current interval.
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
            else:
                # Overlap: remove one interval.
                count += 1
                # Keep interval with smaller end to maximize future compatibility.
                if intervals[i][1] < prev[1]:
                    prev = intervals[i]

        return count
