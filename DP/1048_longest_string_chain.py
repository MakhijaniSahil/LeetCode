"""
LeetCode 1048 - Longest String Chain
Approach 1: Pairwise Comparison
- Sort words by length.
- Compare each word with longer words that are exactly one character longer.
- Check whether the shorter word is a predecessor of the longer word.
Time: O(n^2 * L)
Space: O(n)

Approach 2: Predecessor DP
- Sort words by length.
- For each word, try removing one character at every position.
- If the shorter word exists, extend its chain length.
Time: O(n * L^2)
Space: O(n)
"""

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Sort words so any valid predecessor appears earlier in the array.
        n = len(words)
        words.sort(key=len)
        dp = [1] * n

        # Check whether x is a predecessor of y by allowing one skipped character in y.
        def compare(x, y):
            i, j = 0, 0
            skip = 1
            k = len(x)
            while i < k:
                if x[i] == y[j]:
                    i += 1
                    j += 1
                else:
                    if skip:
                        skip -= 1
                        j += 1
                    else:
                        return False
            return True

        # Compute the best chain starting from each word.
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if len(words[i]) + 1 == len(words[j]):
                    if dp[i] < dp[j] + 1 and compare(words[i], words[j]):
                        dp[i] = dp[j] + 1

        return max(dp)


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Sort by length so every possible predecessor is processed first.
        words.sort(key=len)

        # dp[word] stores the longest chain ending at this word.
        dp = {}
        ans = 1

        # Try removing each character to find a valid predecessor.
        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)

            ans = max(ans, dp[word])

        return ans
