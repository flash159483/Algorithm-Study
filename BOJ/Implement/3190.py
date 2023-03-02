# 3190
# Gold 4

# 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
#
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
#
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
#
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# Example
# Input         Output
# 6             9
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

import sys
import collections

input = sys.stdin.readline

n = int(input())

graph = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

command = {}
for _ in range(int(input())):
    num, c = list(input().split())
    command[int(num)] = c

graph[0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

body = collections.deque()
body.append((0, 0))
time = 0
x = y = 0
while True:
    time += 1
    x = x + dx[dir]
    y = y + dy[dir]
    # 벽에 부딛히거나, 자신의 몸에 부딛힌 경우
    if x == n or x < 0 or y == n or y < 0 or graph[x][y] == 1:
        break
    #사과일때
    if graph[x][y] == 2:
        graph[x][y] = 1
        body.append((x, y))
    else:
        graph[x][y] = 1
        body.append((x, y))
        nx, ny = body.popleft()
        graph[nx][ny] = 0

    if time in command:
        if command[time] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

print(time)