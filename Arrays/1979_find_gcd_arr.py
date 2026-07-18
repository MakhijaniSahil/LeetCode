"""
LeetCode 1979 - Find Greatest Common Divisor of Array
Approach 1: Scan Downward from the Smallest Value
- The gcd of the array must divide both the minimum and maximum values.
- Check candidates from the smaller value down to 1.
- Return the first common divisor found.
Time: O(min(nums))
Space: O(1)

Approach 2: Euclidean Algorithm
- The gcd of the entire array is the gcd of its minimum and maximum values.
- Use the classic Euclidean algorithm to compute it efficiently.
Time: O(log(min(nums)))
Space: O(1)
"""

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort so we can inspect the minimum and maximum values.
        nums.sort()

        s = nums[0]
        l = nums[-1]

        # Try every candidate gcd from the smaller value downward.
        gcd = s
        while gcd > 1:
            if not s % gcd and not l % gcd:
                return gcd
            gcd -= 1

        return 1


class Solution(object):
    def findGCD(self, nums):
        # The gcd of the array is the gcd of its min and max values.
        large = max(nums)
        small = min(nums)

        # Standard Euclidean algorithm.
        while small != 0:
            large, small = small, large % small

        return large
