"""
LeetCode 424 - Longest Repeating Character Replacement
Approach:
- Use a sliding window and keep track of the most frequent character in it.
Time: O(n)
Space: O(1) for fixed alphabet size
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Frequency map for the current window.
        count = {}
        # Highest character frequency seen in the current window.
        max_freq = 0
        # Sliding window boundaries and best answer so far.
        i = j = 0
        res = 0

        # Expand the right edge and shrink the left edge only when needed.
        while j < len(s):
            if s[j] in count:
                count[s[j]] += 1
            else:
                count[s[j]] = 1

            # Track the most common character in the window.
            max_freq = max(max_freq, count[s[j]])

            # If more than k replacements are needed, move i forward.
            if (j - i + 1) - max_freq > k:
                count[s[i]] -= 1
                i += 1

            # Update the best valid window length.
            res = max(res, j - i + 1)
            j += 1
        return res
