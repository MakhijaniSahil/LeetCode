# LeetCode 503 - Next Greater Element II
# Approach: Monotonic decreasing stack on doubled array
# Time: O(n)
# Space: O(n)

from collections import deque

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Duplicate array to simulate circular traversal.
        nums_c = nums*2
        # Map index -> next greater value.
        map = {}
        # Stack stores indices with unresolved next greater element.
        stack = deque()
        for i in range(len(nums_c)):
            # Current value resolves all smaller values on stack top.
            while stack and nums_c[i]>nums_c[stack[-1]]:
                top = stack.pop()
                map[top] = nums_c[i]
            # Keep current index for future comparisons.
            stack.append(i)

        # Build answer for original n indices only.
        res = [map.get(i , -1) for i in range(len(nums))]
        
        return res