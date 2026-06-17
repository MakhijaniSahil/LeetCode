"""
LeetCode 79 - Word Search
Approaches:
- DFS with explicit `visited` matrix to avoid revisiting cells
- DFS with in-place marking and an early frequency-based pruning
Time: Worst-case exponential in word length per start cell
Space: O(rows*cols) for visited or recursion stack
"""

from collections import Counter


class Solution(object):
    def exist(self, board, word):
        """
        DFS using an explicit visited matrix.
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])
        visited = [[0] * cols for _ in range(rows)]

        def dfs(r, c, i):
            # If we've matched all characters
            if i >= len(word):
                return True

            # Out of bounds, visited, or character mismatch
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or visited[r][c]
                or word[i] != board[r][c]
            ):
                return False

            # Mark visited, explore four directions, then unmark
            visited[r][c] = 1
            for dr, dc in moves:
                if dfs(r + dr, c + dc, i + 1):
                    visited[r][c] = 0
                    return True
            visited[r][c] = 0

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


class Solution(object):
    def exist(self, board, word):
        """
        DFS with in-place marking and early pruning using character counts.
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        # Quick rejection if word longer than available cells
        if len(word) > rows * cols:
            return False

        # Early pruning: if board doesn't have enough of any required char
        board_cnt = Counter(char for row in board for char in row)
        word_cnt = Counter(word)
        for ch in word_cnt:
            if word_cnt[ch] > board_cnt[ch]:
                return False

        def dfs(r, c, i):
            if i >= len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            # Temporarily mark the cell as visited by changing its value
            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # Restore original character
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
