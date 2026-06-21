"""
LeetCode 29 - Divide Two Integers
Approach:
- Handle overflow and small edge cases up front
- Work with positive magnitudes and restore the sign at the end
- Repeatedly subtract the largest shifted divisor that still fits
Time: O((log dividend)^2)
Space: O(1)
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        # Fast paths for exact matches and the two one-step divisors.
        if dividend == divisor:
            return 1
        if dividend == -divisor:
            return -1
        if divisor == 1:
            return max(MIN_INT, min(MAX_INT, dividend))
        if divisor == -1:
            return max(MIN_INT, min(MAX_INT, -dividend))
        if dividend == 0:
            return 0

        # Track the sign separately so the core loop can stay on positives.
        sign = True
        if ((dividend < 0) and (divisor > 0)) or ((dividend > 0) and (divisor < 0)):
            sign = False

        p = abs(dividend)
        q = abs(divisor)
        res = 0

        # Subtract the largest power-of-two multiple of the divisor each round.
        while p >= q:
            cnt = 0
            while p >= (q << (cnt + 1)):
                cnt += 1

            res += 1 << cnt
            p -= q * (1 << cnt)

        if sign:
            return min(MAX_INT, res)
        else:
            return max(MIN_INT, -res)
