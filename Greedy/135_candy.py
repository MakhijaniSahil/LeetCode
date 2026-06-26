"""
LeetCode 135 - Candy
Approach:
- Initialize a candies array where each child gets at least 1 candy.
- First pass (left to right): Ensure children with a higher rating than their left neighbor get more candies.
- Second pass (right to left): Ensure children with a higher rating than their right neighbor get more candies, taking the max of current candies and right neighbor's candies + 1.
Time: O(n)
Space: O(n)
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Give every child at least 1 candy initially.
        candies = [1]*len(ratings)

        # Left to right pass to satisfy left neighbor constraints.
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i] = max(candies[i] , candies[i-1]+1)
            
        # Right to left pass to satisfy right neighbor constraints.
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i] = max(candies[i],candies[i+1]+1)
            
        # Total candies needed is the sum of the array.
        return sum(candies) 