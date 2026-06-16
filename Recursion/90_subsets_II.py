"""
LeetCode 90 - Subsets II
Approach: Backtracking with sorting and duplicate skipping
Time: O(n * 2^n)
Space: O(n)
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort so duplicate values are adjacent and easy to skip
        nums.sort()
        res = []
        sub = []

        def dfs(i):
            # Once all numbers are processed, store the current subset
            if i >= len(nums):
                res.append(sub.copy())
                return

            # Include nums[i]
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()

            # Skip all duplicates before exploring the exclude branch
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i] and move forward
            dfs(i + 1)

        dfs(0)
        return res