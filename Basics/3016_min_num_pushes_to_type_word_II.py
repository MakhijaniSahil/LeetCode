"""
LeetCode 3016 - Minimum Number of Pushes to Type Word II
Approach:
- Count how many times each character appears.
- Sort characters by frequency so the most common letters get the cheapest keys.
- Assign letters to keypad tiers of 8 letters each.
Time: O(n log 26)
Space: O(1)
"""

from collections import Counter


class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Count how often each character appears.
        map = Counter(word)

        # Process characters from least frequent to most frequent.
        map_sort = sorted(map, key=lambda c: map[c])

        # Track how many letters have been assigned to the current push tier.
        cnt = 0
        value = 1
        pushes = 0

        # The most frequent characters should get the smallest push cost.
        for i in range(len(map_sort)-1,-1,-1):
            cnt += 1
            pushes += value * map[map_sort[i]]
            if cnt % 8 == 0:
                value += 1

        return pushes
