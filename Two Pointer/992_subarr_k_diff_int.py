"""
LeetCode 992 - Subarrays with K Different Integers
Approach:
- Use a sliding window with exactly k distinct numbers.
- Keep two left pointers to count valid starts for each right pointer.
- Move the near pointer past duplicates while the far pointer marks the first valid start.
Time: O(n)
Space: O(k)
"""

from collections import defaultdict


class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Frequency map for the current window.
        count = defaultdict(int)
        res = 0

        # l_far marks the earliest valid start, l_near trims duplicates.
        l_far = 0
        l_near = 0

        # Expand the right edge of the window.
        for r in range(len(nums)):
            count[nums[r]] += 1

            # Shrink when the window has more than k distinct numbers.
            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near += 1
                l_far = l_near

            # Remove extra copies from the left without changing distinct count.
            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near += 1

            # All starts between l_far and l_near form valid subarrays ending at r.
            if len(count) == k:
                res += l_near - l_far + 1

        return res
