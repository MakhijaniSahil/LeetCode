"""
LeetCode 1406 - Stone Game III
Approach:
- Use recursion with memoization to compute the best score difference from each index.
- On each turn, try taking 1, 2, or 3 stones.
- The current player's score is the stones taken minus the opponent's best response.
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        # Number of piles and memo table for suffix states.
        n = len(stoneValue)
        dp = {}

        # Return the best score difference starting from index i.
        def dfs(i):
            if i == n:
                return 0

            if i in dp:
                return dp[i]

            res = float('-inf')

            # Try taking 1, 2, or 3 stones.
            for j in range(i, min(i + 3, n)):
                res = max(res, sum(stoneValue[i:j + 1]) - dfs(j + 1))

            dp[i] = res
            return res

        res = dfs(0)
        return "Alice" if res>0 else ("Bob" if res<0 else "Tie")
