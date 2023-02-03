# 79. Word Search
# Medium

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Example
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, index):
            if index == len(word):
                return True

            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != word[index]:
                return False

            tmp = board[x][y]
            board[x][y] = '#'
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if dfs(nx, ny, index + 1):
                    return True
            board[x][y] = tmp

        n, m, flag = len(board), len(board[0]), False

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(n):
            for j in range(m):
                if flag == True:
                    break

                if board[i][j] == word[0]:
                    flag = dfs(i, j, 0)

        return flag