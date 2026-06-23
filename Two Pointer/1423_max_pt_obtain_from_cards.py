"""
LeetCode 1423 - Maximum Points You Can Obtain from Cards
Approach:
- Start by taking all k cards from the right side.
- Slide the chosen window by replacing one right card with one left card.
- Track the maximum score across all possible left/right splits.
Time: O(k)
Space: O(1)
"""


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # If all cards must be picked, take the whole array.
        if k == len(cardPoints):
            return sum(cardPoints)

        # Start with all k cards picked from the right end.
        l = 0
        r = len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total

        # Swap one picked right card for one left card at each step.
        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(res, total)
            l += 1
            r += 1

        # Best score among all ways to split k picks between both ends.
        return res
