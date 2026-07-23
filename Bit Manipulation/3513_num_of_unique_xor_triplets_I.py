"""
LeetCode 3513 - Number of Unique XOR Triplets I
Approach:
- The answer depends only on the number of distinct indices available.
- For arrays of size 0, 1, or 2, return the size directly.
- Otherwise, return the smallest power of two that is greater than the array length.
Time: O(log n)
Space: O(1)
"""


class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Only a few elements means the count is just the array size.
        n = len(nums)
        if n <= 2:
            return n

        # Grow powers of two until the result is strictly larger than n.
        res = 1
        while res <= n:
            res<<=1

        return res
