"""
LeetCode 1482 - Minimum Number of Days to Make m Bouquets
Approach:
- Use binary search on the number of days to find the minimum day required.
- The minimum possible day is `min(bloomDay)` and the maximum is `max(bloomDay)`.
- A helper function `possible(d)` greedily checks if we can make `m` bouquets with `k` adjacent flowers on day `d`.
- If it's possible on day `mid`, we try to find a smaller day (search left). Otherwise, we must wait longer (search right).
Time: O(N log(max_day - min_day)) where N is the length of the bloomDay array.
Space: O(1)
"""

class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        # If total flowers required is more than available, it's impossible.
        if m*k>len(bloomDay):
            return -1
        # If total flowers required exactly matches available, we must wait for all to bloom.
        if m*k==len(bloomDay):
            return max(bloomDay)

        def possible(d):
            flowers = 0
            boquets = 0
            for i in bloomDay:
                # If the flower has bloomed by day 'd', count it.
                if i<=d:
                    flowers+=1
                else:
                    # Contiguous streak broken.
                    flowers = 0
                
                # If we have enough contiguous flowers for a bouquet.
                if flowers==k:
                    boquets+=1
                    flowers=0
            
            # Check if we successfully formed at least 'm' bouquets.
            return boquets>=m
        
        # Binary search over the range of possible days.
        l,h = min(bloomDay) , max(bloomDay)
        ans = h
        while l<=h:
            mid = l+(h-l)//2
            
            # If we can make the bouquets, try for an earlier day.
            if possible(mid):
                ans = min(ans,mid)
                h = mid-1
            # Otherwise, we need more days for flowers to bloom.
            else:
                l = mid+1
        return ans