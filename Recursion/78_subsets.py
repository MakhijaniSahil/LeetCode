"""
LeetCode 78 - Subsets
Approach: Backtracking with include/exclude choices
Time: O(n * 2^n)
Space: O(n)
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Current subset being built and the final result list
        res = []
        sub = []

        def dfs(i):
            # Once we process every element, store the current subset
            if i >= len(nums):
                res.append(sub.copy())
                return

            # Include nums[i]
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()

            # Exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res