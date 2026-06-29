"""
LeetCode 410 - Split Array Largest Sum
Approach:
- Use binary search on the answer (the largest sum of any subarray).
- The minimum possible largest sum is `max(nums)` (when k == len(nums)).
- The maximum possible largest sum is `sum(nums)` (when k == 1).
- A helper function `possible(sum)` checks if we can split the array into at most `k` subarrays such that no subarray sum exceeds `sum`.
- If possible with `mid` sum, record it and try to find a smaller sum (search left).
- Otherwise, the sum is too small, requiring more than `k` splits, so we need a larger sum (search right).
Time: O(N log(sum(nums) - max(nums))) where N is the length of nums.
Space: O(1)
"""

class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Base cases for optimization
        if k==1:
            return sum(nums)
        
        if len(nums)==k:
            return max(nums)
        
        def possible(sum):
            cnt = 0
            curr_sum = 0
            i = 0
            while i<len(nums):
                curr_sum+=nums[i]
                # If adding the current element exceeds the allowed sum, 
                # we must start a new subarray.
                if curr_sum>sum:
                    cnt+=1
                    curr_sum = 0
                    continue
                i+=1
            # Count the last accumulated subarray if it's not empty
            if curr_sum:
                cnt+=1
                
            # Check if the number of required subarrays is within the limit k
            return cnt<=k

        # Binary search boundaries
        l = max(nums)
        r = sum(nums)
        res = float('inf')
        
        while l<=r:
            mid = (l+r)//2
            
            # If a valid split exists for this max sum, try to minimize it further
            if possible(mid):
                res = min(mid,res)
                r = mid-1
            # Otherwise, we need a larger max sum to reduce the number of subarrays
            else:
                l = mid+1
            
        return res