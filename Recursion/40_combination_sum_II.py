"""
LeetCode 40 - Combination Sum II
Approach: DFS with sorting and duplicate skipping
Time: Exponential in the worst case
Space: O(target) recursion depth
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Store valid combinations in order as we build them
        res = []

        # Sort so duplicates sit next to each other and can be skipped cleanly
        candidates.sort()

        def dfs(i, curr, target):
            # Found a valid combination
            if target == 0:
                res.append(curr.copy())
                return

            if i >= len(candidates) or target < 0:
                return

            # Take candidates[i] and move to the next index
            curr.append(candidates[i])
            dfs(i + 1, curr, target - candidates[i])
            curr.pop()

            # Skip all duplicates of candidates[i] before exploring the exclude branch
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Exclude candidates[i] and continue
            dfs(i + 1, curr, target)

        dfs(0, [], target)
        return res
