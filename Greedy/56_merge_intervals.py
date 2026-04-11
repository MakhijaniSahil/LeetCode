# LeetCode 56 - Merge Intervals
# Approach: Sort + linear merge scan
# Time: O(n log n)
# Space: O(n)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Store merged output intervals.
        res = []
        n = len(intervals)

        # Sort by start time so overlaps are adjacent.
        intervals.sort()

        # Start with the first interval as current merged block.
        res.append(intervals[0])
        prev = intervals[0]
        for i in range(1, n):
            # Overlap condition: current start <= previous end.
            if prev[1] >= intervals[i][0]:
                prev = [prev[0], max(prev[1], intervals[i][1])]
                res.pop()
                res.append(prev)

            else:
                # No overlap, begin a new merged block.
                res.append(intervals[i])
                prev = intervals[i]

        return res
