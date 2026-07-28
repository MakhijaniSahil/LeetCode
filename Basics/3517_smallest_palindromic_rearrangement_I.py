"""
LeetCode 3517 - Smallest Palindromic Rearrangement I
Approach:
- Count the frequency of each character.
- Place half of each character on the left side of the palindrome.
- If a character has an odd count, keep one copy in the middle.
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count occurrences of each lowercase character.
        cnt = [0] * 26

        for c in s:
            idx = ord(c) - ord('a')
            cnt[idx] += 1

        # Build the left half and remember the odd-count middle character.
        res = ""
        middle = None
        for i, v in enumerate(cnt):
            if v % 2 != 0:
                middle = chr(i + 97)
            res += chr(i + 97) * (v // 2)

        # Mirror the left half to complete the palindrome.
        rev_res = res[::-1]
        if middle:
            res += middle

        return res + rev_res
