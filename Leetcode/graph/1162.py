# 1162. As Far from Land as Possible
# Medium

# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized,
# and return the distance. If no land or water exists in the grid, return -1.
#
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
#

# Example
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land = collections.deque()
        water = 0
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j] == 1:
                    land.append((i, j))
                else:
                    water += 1

        if water == 0 or len(land) == 0:
            return -1

        def bfs():
            result = 0
            while land:
                for _ in range(len(land)):
                    x, y = land.popleft()
                    for i in range(4):
                        nx, ny = dx[i] + x, dy[i] + y
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                            grid[nx][ny] = 1
                            land.append((nx, ny))

                result += 1
            return result

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        return bfs() - 1
