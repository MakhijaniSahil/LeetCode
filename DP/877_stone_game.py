"""
LeetCode 877 - Stone Game
Approach 1: Memoized Recursion
- Compute the maximum stones the current player can collect from a subarray.
- The parity of the remaining interval determines whether the current pick contributes.
- Compare the first player's best total with half the sum of all piles.
Time: O(n^2)
Space: O(n^2)

Approach 2: Direct Result
- For this problem, the first player can always win.
Time: O(1)
Space: O(1)
"""

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # Memo table for subarray results.
        dp = {}

        # Return the maximum stones the current player can get from piles[l..r].
        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            # Determine whether the current move contributes stones for this parity.
            even = True if (r - 1) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)

            return dp[(l, r)]

        # First player wins if they can collect more than half the stones.
        return dfs(0, len(piles) - 1) > (sum(piles)) // 2


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # The first player can always force a win for this problem.
        return True
