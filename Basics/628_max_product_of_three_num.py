"""
LeetCode 628 - Maximum Product of Three Numbers
Approach:
- Sort the array once.
- The answer is either the product of the three largest numbers.
- Or it is the product of the two smallest numbers and the largest number.
Time: O(n log n)
Space: O(1)
"""


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort so we can inspect both ends of the array.
        nums.sort()

        # Compare the best positive-only product with the two-negative case.
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
