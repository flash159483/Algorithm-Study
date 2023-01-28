#2206
#gold 3

# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
#
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
#
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
#
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

#input                      #output
# 6 4                       15
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

import sys
import collections


def bfs():
    q = collections.deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, c = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[x][y][c])
            return
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and c == 0:
                q.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][0] + 1

            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] + 1
                q.append((nx, ny, c))
    print(-1)


n, m = map(int, input().split())
graph = []
walls = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    tmp = []
    for j in range(m):
        if graph[i][j] == 1:
            tmp.append([i, j])
    walls.extend(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

bfs()

