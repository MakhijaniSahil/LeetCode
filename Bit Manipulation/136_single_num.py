"""
LeetCode 136 - Single Number
Approach:
- XOR every value together
- Equal pairs cancel out, leaving the unique value
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            # XOR cancels out duplicates and preserves the unmatched value.
            res ^= n

        return res