"""
LeetCode 127 - Word Ladder
Approach:
- Run a BFS from the begin word.
- Generate all one-letter transformations for each word.
- Remove words from the dictionary as soon as they are queued to avoid revisiting them.
Time: O(N * L * 26)
Space: O(N)
"""

from collections import deque
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Use a set for O(1) membership checks.
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        # BFS queue stores (current word, ladder length so far).
        n = len(beginWord)
        q = deque([(beginWord, 1)])

        while q:
            curr, length = q.popleft()

            # The first time we reach the end word is the shortest ladder.
            if curr == endWord:
                return length

            # Try changing every character to every lowercase letter.
            for i in range(n):
                for c in string.ascii_lowercase:
                    if c == curr[i]:
                        continue

                    nei = curr[:i] + c + curr[i+1:]

                    if nei in wordSet:
                        q.append((nei, length + 1))
                        # Mark as visited when enqueued to avoid duplicate work.
                        wordSet.remove(nei)

        return 0
