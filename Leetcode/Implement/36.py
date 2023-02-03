# 36. Valid Sudoku
# Medium

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rowValid():
            for i in range(9):
                check = set()
                for j in range(9):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in check:
                        return False
                    check.add(board[i][j])
            return True

        def colValid():
            for i in range(9):
                check = set()
                for j in range(9):
                    if board[j][i] == '.':
                        continue
                    if board[j][i] in check:
                        return False
                    check.add(board[j][i])
            return True

        def boxValid(x, y, n):
            if n == 3:
                check = set()
                for i in range(x, x + n):
                    for j in range(y, y + n):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in check:
                            return False
                        check.add(board[i][j])
            else:
                n = n // 3
                for i in range(3):
                    for j in range(3):
                        if not boxValid(x + n * i, y + n * j, n):
                            return False

            return True

        return all([colValid(), rowValid(), boxValid(0, 0, 9)])