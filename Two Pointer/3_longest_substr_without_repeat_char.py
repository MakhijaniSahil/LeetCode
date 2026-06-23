"""
LeetCode 3 - Longest Substring Without Repeating Characters
Approach:
- Use a sliding window with character frequencies.
- Expand the right edge and shrink from the left when a duplicate appears.
- Track the maximum valid window length.
Time: O(n)
Space: O(min(n, charset))
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Empty string has no substring.
        if not s:
            return 0

        # Frequency map for characters in the current window.
        count = {}

        # Sliding window left boundary and best answer so far.
        i = 0
        res = 0

        # Expand the right edge of the window.
        for j in range(len(s)):
            if s[j] not in count:
                count[s[j]] = 1
            else:
                count[s[j]] += 1

                # Shrink until the duplicate character is removed.
                while count[s[j]] > 1:
                    count[s[i]] -= 1
                    i += 1

            # Current window has all unique characters.
            res = max(res, j - i + 1)

        return res
