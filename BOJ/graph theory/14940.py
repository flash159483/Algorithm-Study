# 14940
# Silver 1

# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
#
# 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.


import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
dist = [[-1] * m for _ in range(n)]

start = ()

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
        elif graph[i][j] == 0:
            dist[i][j] = 0


q = collections.deque([start])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist[start[0]][start[1]] = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))


for i in dist:
    print(*i)