"""
LeetCode 3731 - Find Missing Elements
Approach:
- Sort the array so gaps are easy to detect.
- Walk from the smallest value to the largest value.
- Whenever the expected value does not match the current array value, record it as missing.
Time: O(n log n)
Space: O(1)
"""


class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Sort the numbers to scan them in order.
        nums.sort()
        i = nums[0]
        j = nums[-1]
        n = len(nums)
        k = 0
        res = []

        # Compare the expected value with the current array value.
        while k<n:
            if nums[k] != i:
                res.append(i)
                i += 1
                continue
            i += 1
            k += 1

        return res
