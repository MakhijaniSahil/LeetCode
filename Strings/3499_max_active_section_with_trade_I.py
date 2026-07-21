"""
LeetCode 3499 - Max Active Section With Trade I
Approach:
- Count the current active cells.
- Record the lengths of all consecutive inactive blocks.
- The best trade combines two neighboring inactive blocks into one larger active section.
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Total length and current number of active cells.
        n = len(s)
        activeCnt = s.count('1')

        # Store the length of every consecutive block of inactive cells.
        inactiveBlock = []

        # Scan the string and compress runs of zeroes.
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                inactiveBlock.append(i-start)

            else:
                i += 1

        # The trade only affects two adjacent inactive blocks.
        maxSum = 0

        for i in range(1, len(inactiveBlock)):
            maxSum = max(maxSum, inactiveBlock[i] + inactiveBlock[i - 1])

        return maxSum + activeCnt
