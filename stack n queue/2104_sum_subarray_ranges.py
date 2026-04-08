# LeetCode 2104 - Sum of Subarray Ranges
# Approach: Monotonic stacks (sum of maxima - sum of minima)
# Time: O(n)
# Space: O(n)
from collections import deque


class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Accumulate total contribution as minimum and maximum separately.
        min_sum = 0
        max_sum = 0

        # Add sentinels to flush stacks at boundaries.
        nums1 = [float("-inf")] + nums + [float("-inf")]
        nums2 = [float("inf")] + nums + [float("inf")]

        # Increasing stack for minimum contributions.
        min_stack = deque()
        # Decreasing stack for maximum contributions.
        max_stack = deque()

        for i in range(len(nums1)):
            # Current value resolves next smaller element for min-stack indices.
            while min_stack and nums1[i] < nums1[min_stack[-1]]:
                j = min_stack.pop()
                left = j - min_stack[-1]
                right = i - j
                min_sum += nums1[j] * left * right
            min_stack.append(i)

            # Current value resolves next greater element for max-stack indices.
            while max_stack and nums2[i] > nums2[max_stack[-1]]:
                j = max_stack.pop()
                left = j - max_stack[-1]
                right = i - j
                max_sum += nums2[j] * left * right
            max_stack.append(i)

        # Total range sum = sum of all subarray maximums - sum of all subarray minimums.
        return max_sum - min_sum
