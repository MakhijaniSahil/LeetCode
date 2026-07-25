"""
LeetCode 3536 - Maximum Product of Two Digits
Approach:
- Convert the number into a list of digits.
- Sort the digits and multiply the two largest ones.
Time: O(d log d)
Space: O(d)
"""


class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Split the number into individual digits.
        arr = list(map(int, str(n)))

        # Sort so the largest digits are at the end.
        arr.sort()

        return arr[-1] * arr[-2]
