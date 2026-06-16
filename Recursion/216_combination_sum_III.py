"""
LeetCode 216 - Combination Sum III
Approach: Backtracking over numbers 1..9, choose k numbers summing to n
Time: Combinatorial (bounded) - at most C(9,k) branches
Space: O(k) recursion depth
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        # Candidate numbers are 1..9
        nums = list(range(1, 10))
        sub = []
        cnt = k

        def dfs(i, target):
            # If we've hit the target and used exactly k numbers, record result
            if target == 0 and len(sub) == cnt:
                res.append(sub.copy())
                return

            # Prune branches that cannot lead to a valid solution
            if target < 0 or i >= len(nums) or len(sub) == cnt:
                return

            # Choose nums[i]
            sub.append(nums[i])
            dfs(i + 1, target - nums[i])
            sub.pop()

            # Skip nums[i]
            dfs(i + 1, target)

        dfs(0, n)
        return res
