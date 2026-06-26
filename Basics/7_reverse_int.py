"""
LeetCode 7 - Reverse Integer
Approach:
- Handle the sign separately by taking the absolute value of the integer.
- Extract digits one by one from the end using modulo 10 and build the reversed number.
- Restore the original sign after the loop.
- Check if the reversed number falls outside the 32-bit signed integer range, and return 0 if it does.
Time: O(log(x))
Space: O(1)
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit signed integer bounds to check for overflow.
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        # Keep track of the sign of the original number.
        sign = False
        if x<0:
            sign = True

        # Work with the absolute value to make digit extraction easier.
        x = abs(x)
        rev = 0
        # Pop digits from the end and push them to the reversed number.
        while x>0:
            rev = rev*10 + x%10
            x//=10

        # Restore the sign of the reversed number.
        if sign:
            rev = -rev
        
        # Return 0 if the reversed number causes an overflow.
        if rev > INT_MAX or rev<INT_MIN:
            return 0
        
        return rev