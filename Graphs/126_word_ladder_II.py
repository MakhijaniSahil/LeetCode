"""
LeetCode 126 - Word Ladder II
Approach 1: DFS with Backtracking
- Try every one-letter transformation recursively.
- Track the current best ladder length and keep only shortest sequences.
- This approach is correct but too slow for large inputs.
Time: TLE
Space: O(N)

Approach 2: BFS + Backtracking
- First run BFS to record the shortest distance to each reachable word.
- Then backtrack from the end word to the begin word using only distance-decreasing edges.
- This guarantees that only shortest ladders are collected.
Time: O(N * L * 26)
Space: O(N)
"""

from collections import deque
import string


class Solution(object): # Got TLE
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # Dictionary of valid intermediate words.
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # Track the shortest sequence length found so far.
        n = len(beginWord)
        res = []
        maxLen = [float('inf')]
        currSeq = [beginWord]

        # Explore all possible paths recursively.
        def dfs(node, ln, currSeq):
            if node == endWord:
                if ln < maxLen[0]:
                    res[:] = [currSeq[:]]
                    maxLen[0] = ln
                elif ln == maxLen[0]:
                    res.append(currSeq[:])
                return

            for i in range(n):
                for c in string.ascii_lowercase:
                    if c == node[i]:
                        continue

                    nei = node[:i] + c + node[i+1:]

                    if nei in wordSet:
                        wordSet.remove(nei)
                        dfs(nei, ln + 1, currSeq + [nei])
                        wordSet.add(nei)

        dfs(beginWord, 1, currSeq)
        return res


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # dist[word] stores the shortest distance from beginWord to word.
        dist = {}
        dist[beginWord] = 1
        n = len(beginWord)
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        q = deque([beginWord])

        # BFS discovers shortest distances to every reachable word.
        while q:
            size = len(q)
            used = set()

            for _ in range(size):
                curr = q.popleft()

                for i in range(n):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == curr[i]:
                            continue

                        newWord = curr[:i] + c + curr[i + 1:]

                        if newWord in wordSet:
                            if newWord not in dist:
                                dist[newWord] = dist[curr] + 1
                                q.append(newWord)
                                used.add(newWord)

            # Remove words once the current BFS layer finishes.
            wordSet -= used

            if endWord in dist:
                break

        if endWord not in dist:
            return []

        ans = []

        # Backtrack only along edges that decrease the distance by one.
        def dfs(curr, path):
            if curr == beginWord:
                ans.append(path[::-1])
                return

            for i in range(n):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == curr[i]:
                        continue

                    prev = curr[:i] + c + curr[i + 1:]

                    if prev in dist and dist[prev] == dist[curr] - 1:
                        path.append(prev)
                        dfs(prev, path)
                        path.pop()

        dfs(endWord, [endWord])
        return ans
