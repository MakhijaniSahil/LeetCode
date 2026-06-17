"""
LeetCode 51 - N-Queens
Approach: Backtracking with column and diagonal pruning
Time: Exponential in n
Space: O(n)
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # Track occupied columns and diagonals so we can prune invalid placements
        col = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # If all rows are filled, we found one valid board configuration
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place a queen and mark the constraints as used
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Remove the queen and backtrack to try the next column
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
