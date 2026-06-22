"""
LeetCode 1358 - Number of Substrings Containing All Three Characters
Approach 1: Sliding Window with Frequency Map
- Expand the window until all three characters are present.
- Shrink from the left and count all valid subarrays.
Time: O(n)
Space: O(1)

Approach 2: Track Last Seen Indices
- Maintain the index of the most recent occurrence of 'a', 'b', 'c'.
- Any substring starting before the minimum of these indices is valid.
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Frequency of each character in the current window.
        count = {"a": 0, "b": 0, "c": 0}
        res = 0
        i = 0

        # Expand the window with the right pointer.
        for j in range(len(s)):
            count[s[j]] += 1

            # Shrink the window while all three characters are present.
            while all(count[c] > 0 for c in "abc"):
                count[s[i]] -= 1
                i += 1

            # All substrings starting at i or later and ending at j are valid.
            res += i
        return res

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Track the last seen index of each character.
        last_a = last_b = last_c = -1
        res = 0

        # Update the last seen index and count valid starting positions.
        for i, char in enumerate(s):
            if char == "a":
                last_a = i
            elif char == "b":
                last_b = i
            else:  # char == 'c'
                last_c = i

            # Any substring starting before the minimum index is valid.
            res += min(last_a, last_b, last_c) + 1

        return res
