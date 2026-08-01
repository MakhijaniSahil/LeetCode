"""
LeetCode 486 - Predict the Winner
Approach:
- Use recursion to compute the best score the current player can guarantee from any subarray.
- On each turn, the player picks either end and the opponent then plays optimally.
- Compare player 1's score with the remaining total score.
Time: O(n^2)
Space: O(n^2)
"""


class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Total points available and number of elements.
        total = sum(nums)
        n = len(nums)

        # Return the maximum score the current player can obtain from nums[i..j].
        def solve(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i]

            # Pick the left or right value, assuming the opponent minimizes our future score.
            take_i = nums[i] + min(solve(i + 2, j), solve(i + 1, j - 1))
            take_j = nums[j] + min(solve(i, j - 2), solve(i + 1, j - 1))

            return max(take_i, take_j)

        # Compare player 1's best total with player 2's remaining total.
        p1 = solve(0, n - 1)
        p2 = total - p1

        return p1 >= p2
