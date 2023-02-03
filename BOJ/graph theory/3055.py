# 3055
# gold 4

# 사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다.
# 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.
#
# 티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다.
# 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.
#
# 매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다.
# 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.
#
# 티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.
#
# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.

# Example
# Input:            output:
# 3 3               3
# D.*
# ...
# .S.

import sys
import collections

input = sys.stdin.readline


def flood():
    for _ in range(len(water)):
        x, y = water.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '.':
                    water.append((nx, ny))
                    graph[nx][ny] = '*'
                    visited[nx][ny] = -1


def bfs():
    while tmp:
        for _ in range(len(tmp)):
            x, y = tmp.popleft()

            if graph[x][y] != '*':
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 'D':
                            return visited[x][y] + 1
                        elif graph[nx][ny] == '.' and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            tmp.append((nx, ny))
        flood()
    return 'KAKTUS'


n, m = map(int, input().split())
tmp = collections.deque()
water = collections.deque()
graph = []
visited = [[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(m):
        if graph[i][j] == 'S':
            tmp.append([i, j])
        elif graph[i][j] == '*':
            water.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())

