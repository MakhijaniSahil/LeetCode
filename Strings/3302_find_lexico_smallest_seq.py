"""
LeetCode 3302 - Find the Lexicographically Smallest Sequence
Approach:
- Precompute how many characters of word2 can still be matched from each suffix of word1.
- Scan word1 from left to right and greedily match word2.
- Allow one flexible choice when needed, as long as the remaining suffix can still complete the sequence.
Time: O(n + m)
Space: O(n)
"""


class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        # Lengths of the two words.
        n = len(word1)
        m = len(word2)

        # rtSideMatchLen[i] = how many characters of word2 can be matched from word1[i:].
        rtSideMatchLen = [0] * n

        # Build suffix match counts from right to left.
        rtMatched = 0
        i = n-1
        j = m-1

        while i >= 0:
            if j >= 0 and word1[i] == word2[j]:
                rtMatched += 1
                j -= 1

            rtSideMatchLen[i] = rtMatched
            i -= 1

        # Greedily match word2 from left to right.
        res = []
        changePow = True

        i = 0
        j = 0

        while i < n and j < m:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif changePow and i + 1 < n and rtSideMatchLen[i + 1] >= m - j - 1:
                res.append(i)
                j += 1
                changePow = False

            i += 1

        return res if j == m else []
