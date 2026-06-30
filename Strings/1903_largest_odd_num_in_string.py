"""
LeetCode 1903 - Largest Odd Number in String
Approach:
- A number is odd if and only if its last digit is odd.
- To find the largest odd number that is a substring of `num`, we should find the rightmost odd digit in the string.
- Iterate from right to left, and as soon as an odd digit is found, return the prefix of the string up to and including this digit.
Time: O(N) where N is the length of the string
Space: O(1) (excluding the space needed to return the substring)
"""

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # Iterate backwards through the string
        for i in range(len(num)-1, -1, -1):
            # Check if the current digit is odd
            if int(num[i])%2!=0:
                # Return the substring from the beginning up to the odd digit
                return num[:i+1]
                
        # If no odd digit is found, return an empty string
        return ""