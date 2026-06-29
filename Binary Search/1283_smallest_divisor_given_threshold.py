"""
LeetCode 1283 - Find the Smallest Divisor Given a Threshold
Approach:
- Use binary search on the answer space (the divisor).
- The minimum possible divisor is 1, and the maximum is `max(nums)`.
- A helper function `check(div)` calculates the sum of divisions (rounded up) for a given divisor `div`.
- If the sum is <= threshold, it's a valid divisor, so we record it and try to find a smaller one (search left).
- Otherwise, the divisor is too small (causing the sum to be too large), so we need a larger divisor (search right).
Time: O(N log(max(nums))) where N is the length of the nums array.
Space: O(1)
"""

import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def check(div):
            # Calculate the sum of elements divided by div, rounded up.
            sum = 0
            for n in nums:
                sum+=math.ceil(n/div)
            return sum<=threshold

        # Minimum and maximum possible divisors.
        l,h = 1,max(nums)
        res = float('inf')
        
        while l<=h:
            # Prevent potential overflow.
            mid = l + (h-l)//2
            
            # If the current divisor is valid, try for a smaller one.
            if check(mid):
                res = min(mid,res)
                h = mid-1
            # If invalid (sum too large), increase the divisor.
            else:
                l=mid+1
        return res