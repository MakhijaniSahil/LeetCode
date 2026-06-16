"""
LeetCode 39 - Combination Sum
Approach 1: Recursive search with deduplication by sorting
Approach 2: Standard DFS with index control to avoid duplicates
Time: Exponential in the worst case
Space: O(target) recursion depth
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Store combinations as sorted tuples to avoid duplicate paths
        res = set()

        def recur(path, target):
            # Found a valid combination
            if target == 0:
                res.add(tuple(sorted(path)))
                return

            if target < 0:
                return

            for c in candidates:
                if c > target:
                    continue
                curr_path = path + [c]
                if tuple(sorted(curr_path)) in res:
                    continue
                recur(curr_path, target - c)

        for c in candidates:
            if c > target:
                continue
            curr_path = [c]
            recur(curr_path, target - c)

        return [list(x) for x in res]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Result list for all valid combinations
        res = []

        def dfs(i, curr, target):
            # Exact target reached, store a copy of the current path
            if target == 0:
                res.append(curr.copy())
                return

            if i >= len(candidates) or target < 0:
                return

            # Take candidates[i] and stay at the same index to allow reuse
            curr.append(candidates[i])
            dfs(i, curr, target - candidates[i])
            curr.pop()
            # Skip candidates[i] and move to the next candidate
            dfs(i + 1, curr, target)

        dfs(0, [], target)
        return res
