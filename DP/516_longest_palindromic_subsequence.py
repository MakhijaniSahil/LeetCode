"""
LeetCode 516 - Longest Palindromic Subsequence
Approach 1: Plain Recursion
- Compare the two ends of the string.
- If they match, take both ends and recurse inward.
- Otherwise, skip one end and take the better result.
Time: TLE
Space: O(n)

Approach 2: LCS with Reversed String
- The longest palindromic subsequence is the LCS of the string and its reverse.
- Build a classic 2D dynamic programming table.
Time: O(n^2)
Space: O(n^2)

Approach 3: Memoized Recursion
- Use the same two-end recursion as the first approach.
- Cache overlapping subproblems in a 2D table.
Time: O(n^2)
Space: O(n^2)
"""

class Solution(object): #Got TLE
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Plain recursion over substring boundaries.
        def dfs(i,j):
            if i > j:
                return 0

            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + dfs(i + 1, j - 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))

        return dfs(0, len(s) - 1)


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Reverse string turns the problem into LCS.
        n = len(s)
        x = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Standard LCS transition between s and reversed s.
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == x[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Memoized top-down DP over substring boundaries.
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def dfs(i,j):
            if i > j:
                return 0

            if i == j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = 2 + dfs(i + 1, j - 1)
                return dp[i][j]
            else:
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j - 1))
                return dp[i][j]

        return dfs(0, len(s) - 1)
