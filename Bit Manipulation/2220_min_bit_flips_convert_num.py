"""
LeetCode 2220 - Minimum Bit Flips to Convert Number
Approach:
- XOR marks the bits that differ between `start` and `goal`
- `bit_count()` returns how many differing bits need to be flipped
Time: O(1)
Space: O(1)
"""


class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        # Count the number of differing bits between the two numbers.
        return (start ^ goal).bit_count()
