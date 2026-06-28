"""
LeetCode 875 - Koko Eating Bananas
Approach:
- Use binary search on the eating speed `k`.
- The minimum possible speed is 1, and the maximum is the size of the largest pile.
- For a given speed `mid`, calculate the total hours required to eat all bananas.
- If the total hours <= `h`, it's a valid speed, so we try to find a smaller speed (search left).
- Otherwise, the speed is too slow, so we need a faster speed (search right).
Time: O(n log(m)) where n is the number of piles and m is the maximum pile size.
Space: O(1)
"""

import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # Minimum possible eating speed is 1.
        l = 1
        # Maximum possible eating speed is the largest pile.
        r = max(piles)
        # Store the minimum valid speed found so far.
        res = r

        while l<=r:
            mid = l + (r-l)//2
            total = 0
            
            # Calculate total hours needed to eat all piles at speed 'mid'.
            for i in piles:
                total+= math.ceil(i/mid)
                
            # If Koko can finish within h hours, try to find a slower valid speed.
            if total<=h:
                res = min(res,mid)
                r=mid-1
            # If it takes too long, Koko must eat faster.
            else:
                l=mid+1
        
        return res