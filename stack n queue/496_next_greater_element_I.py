# LeetCode 496 - Next Greater Element I
# Approach: Monotonic decreasing stack over nums2
# Time: O(len(nums1) + len(nums2))
# Space: O(len(nums2))

from collections import deque

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Map each number in nums2 to its next greater element.
        map = {}
        # Decreasing stack: top is the most recent unresolved number.
        stack = deque()

        for n in nums2:
            # Current number is the next greater for all smaller stack values.
            while stack and n > stack[-1]:
                top = stack.pop()
                map[top] = n
            # Keep unresolved numbers for future comparisons.
            stack.append(n)

        # Build answer for nums1 using precomputed next greater values.
        res = []
        for n in nums1:
            if n in map:
                res.append(map[n])
            else:
                res.append(-1)

        return res
