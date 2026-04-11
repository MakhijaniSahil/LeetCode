# LeetCode 57 - Insert Interval
# Approach: Linear scan with merge while overlapping
# Time: O(n)
# Space: O(n)


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Store final merged interval list.
        res = []
        n = len(intervals)
        i = 0

        # Add intervals that end before newInterval starts.
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        # Merge all intervals overlapping with newInterval.
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged newInterval.
        res.append(newInterval)

        # Append remaining intervals that start after merged interval.
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
