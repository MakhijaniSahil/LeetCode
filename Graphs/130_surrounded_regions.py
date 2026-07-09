"""
LeetCode 130 - Surrounded Regions
Approach:
- Start DFS from every border `O` and mark all connected `O`s as safe.
- Flip the remaining `O`s to `X` because they are fully surrounded.
- Restore the safe cells back to `O` at the end.
Time: O(m * n)
Space: O(m * n)
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Board dimensions.
        m = len(board)
        n = len(board[0])

        # Mark border-connected regions as safe.
        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or board[r][c] != "O":
                return
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Only border cells can escape being captured.
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r in [0, m - 1] or c in [0, n - 1]):
                    dfs(r,c)

        # Flip enclosed regions to X and restore safe cells back to O.
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
