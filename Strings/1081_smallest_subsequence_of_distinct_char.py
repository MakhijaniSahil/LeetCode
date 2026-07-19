"""
LeetCode 1081 - Smallest Subsequence of Distinct Characters
Approach:
- Scan the string and build the answer with a monotonic stack.
- Skip characters that are already in the result.
- While the stack top is larger than the current character and appears later again, pop it to get a lexicographically smaller result.
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Length of the input string.
        n = len(s)

        # taken tracks whether a character is already in the subsequence.
        taken = [False] * 26
        # lastIdx stores the last position of each character.
        lastIdx = [-1] * 26
        res = []

        # Record the last occurrence of every character.
        for i in range(n):
            c = s[i]
            lastIdx[ord(c) - ord('a')] = i

        # Build the smallest valid subsequence.
        for i in range(n):
            c = s[i]
            idx = ord(c) - ord('a')

            if taken[idx]:
                continue

            # Pop larger characters if they still appear later in the string.
            while res and ord(res[-1]) > ord(c) and lastIdx[ord(res[-1]) - ord('a')] > i:
                taken[ord(res[-1]) - ord('a')] = False
                res.pop()

            res.append(c)
            taken[idx] = True

        return "".join(res)
