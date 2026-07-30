"""
LeetCode 3014 - Minimum Number of Pushes to Type Word I
Approach:
- Assign the cheapest cost to the first 8 letters, then the next 8, and so on.
- Count the characters in the word in order of appearance.
- Every block of 8 characters increases the push cost by 1.
Time: O(n)
Space: O(1)
"""


class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # cnt tracks how many characters have been assigned to the current cost tier.
        cnt = 0
        pushes = 0
        value = 1

        # Add the current typing cost for each character.
        for i in range(len(word)):
            cnt += 1
            pushes += value
            if cnt % 8 == 0:
                value += 1

        return pushes
