# 695. Max Area of Island
# Medium

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
#                                                                     'You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
#                [0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            grid[i][j] = 0
            result = 0

            while q:
                x, y = q.popleft()
                result += 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0:
                        grid[nx][ny] = 0
                        q.append((nx, ny))
            return result

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tmp = bfs(i, j)
                    ans = max(tmp, ans)

        return ans
