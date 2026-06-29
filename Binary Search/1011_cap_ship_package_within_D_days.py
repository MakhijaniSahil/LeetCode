"""
LeetCode 1011 - Capacity To Ship Packages Within D Days
Approach:
- Use binary search on the answer space (the ship's weight capacity).
- The minimum possible capacity is `max(weights)` (must be able to carry the heaviest package).
- The maximum possible capacity is `sum(weights)` (can carry all packages in one day).
- A helper function `possible(cap)` checks if a given capacity can ship all packages within `days` days.
- If it's possible with `mid` capacity, try to find a smaller capacity (search left).
- Otherwise, the capacity is too small, so increase it (search right).
Time: O(N log(sum(weights) - max(weights))) where N is the length of the weights array.
Space: O(1)
"""

class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def possible(cap):
            # Track current weight on the ship and days taken.
            total = 0
            d = 1
            for w in weights:
                total+=w
                # If adding this package exceeds capacity, it must go on the next day.
                if total>cap:
                    d+=1
                    total = w
            
            # Check if total days required is within the allowed days limit.
            return d<=days

        # Binary search space for capacity.
        l=max(weights)
        r=sum(weights)
        res=float('inf')
        
        while l<=r:
            mid = (l+r)//2
            
            # If valid, record the capacity and try a smaller one.
            if possible(mid):
                res = min(res,mid)
                r=mid-1
            # If invalid, we need a larger capacity.
            else:
                l=mid+1
        return res