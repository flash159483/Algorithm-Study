# 7562
# Silver 1

# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# Example
# Input         Output
# 3             5
# 8             28
# 0 0           0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1

import collections
import sys


def bfs():
    q = collections.deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            print(visited[x][y]-1)
        for i in range(8):
            nx = dx[i]+x
            ny = dy[i]+y

            if nx < 0 or nx >= l or ny < 0 or ny >= l or visited[nx][ny] != 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] += visited[x][y] + 1


n = int(input())

for _ in range(n):
    l = int(input())
    start_x, start_y = map(int, sys.stdin.readline().rstrip().split())
    end_x, end_y = map(int, sys.stdin.readline().rstrip().split())

    if start_x == end_x and start_y == end_y:
        print(0)
        continue

    visited = [[0]*l for __ in range(l)]
    dx = [-1, 1, -2, 2, -1, 1, -2, 2]
    dy = [2, 2, 1, 1, -2, -2, -1, -1]

    bfs()
