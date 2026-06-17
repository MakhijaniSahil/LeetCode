"""
LeetCode 37 - Sudoku Solver
Approach: Backtracking with constraint tracking for rows, columns, and 3x3 boxes
Time: Worst-case exponential, but highly pruned in practice
Space: O(1) extra space (modifies board in-place)
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Track which numbers are used in each row, column, and 3x3 box
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        # Initialize constraint sets with given numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    row[r].add(num)
                    col[c].add(num)
                    box_idx = (r // 3) * 3 + (c // 3)
                    box[box_idx].add(num)

        def backtrack(r, c):
            # If we filled all 9 rows, puzzle is solved
            if r == 9:
                return True

            # Move to next row when we reach the end of current row
            if c == 9:
                return backtrack(r + 1, 0)

            # Skip cells that are already filled
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            # Try digits 1-9 in this cell
            for n in range(1, 10):
                box_idx = (r // 3) * 3 + (c // 3)
                if n in col[c] or n in row[r] or n in box[box_idx]:
                    continue

                # Place the digit and update constraint sets
                board[r][c] = str(n)
                row[r].add(n)
                col[c].add(n)
                box[box_idx].add(n)

                if backtrack(r, c + 1):
                    return True

                # Backtrack: remove the digit and restore state
                board[r][c] = "."
                row[r].remove(n)
                col[c].remove(n)
                box[box_idx].remove(n)

            return False

        backtrack(0, 0)