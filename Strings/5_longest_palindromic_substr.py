"""
LeetCode 5 - Longest Palindromic Substring
Approach:
- Center expansion: expand around each index (odd-length centers)
  and each gap between indices (even-length centers).
- Track the longest palindrome seen while expanding.
Time: O(n^2) worst-case (e.g., all same characters)
Space: O(1) excluding output
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        # Expand around every possible center. For odd-length palindromes
        # the center is at i (l == r == i). For even-length, center is
        # between i and i+1 (l == i, r == i+1).
        for i in range(len(s)):
            # odd length center
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > resLen:
                    res = s[l : r + 1]
                    resLen = cur_len
                l -= 1
                r += 1

            # even length center
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > resLen:
                    res = s[l : r + 1]
                    resLen = cur_len
                l -= 1
                r += 1

        return res