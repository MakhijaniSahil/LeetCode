"""
LeetCode 78 - Subsets
Approach:
- Bit manipulation: iterate through all 2^n binary masks
- For each mask, check which bits are set and include corresponding elements
Time: O(n * 2^n)
Space: O(1) excluding the output
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        subsets = 1 << n  # There are 2^n subsets.
        ans = []

        # Iterate through all possible binary masks from 0 to 2^n - 1.
        for num in range(subsets):
            curr_sub = []
            for i in range(n):
                # If bit i is set in the current mask, include nums[i].
                if num & (1 << i):
                    curr_sub.append(nums[i])

            ans.append(curr_sub)

        return ans
