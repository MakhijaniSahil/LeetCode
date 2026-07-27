"""
LeetCode 1464 - Maximum Product of Two Elements in an Array
Approach:
- Sort the array.
- Use the two largest values, subtract 1 from each, and multiply them.
Time: O(n log n)
Space: O(1)
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort so the two largest elements are at the end.
        nums.sort()

        # Return the product of the two largest adjusted values.
        return (nums[-1]-1)*(nums[-2]-1)
