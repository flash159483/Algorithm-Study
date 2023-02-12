# 1706. Where Will the Ball Fall
# Medium

# You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.
#
# Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.
#
# A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
# A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
# We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom.
# A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.
#
# Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top,
# or -1 if the ball gets stuck in the box.

# Example
# Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# Output: [1,-1,-1,-1,-1]
# Explanation: This example is shown in the photo.
# Ball b0 is dropped at column 0 and falls out of the box at column 1.
# Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
# Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
# Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
# Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        result = [0] * m

        def dfs(x, y, start):
            if x == n:
                result[start] = y
                return
            if grid[x][y] == 1 and y == m - 1:
                result[start] = -1
            elif grid[x][y] == -1 and y == 0:
                result[start] = -1
            elif grid[x][y] == 1 and grid[x][y + 1] == -1:
                result[start] = -1
            elif grid[x][y] == -1 and grid[x][y - 1] == 1:
                result[start] = -1
            else:
                if grid[x][y] == 1:
                    dfs(x + 1, y + 1, start)
                else:
                    dfs(x + 1, y - 1, start)

        for i in range(m):
            dfs(0, i, i)

        return result
