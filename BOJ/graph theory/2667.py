# 2667
# silver 1

# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# Example
#input              output
# 7                 3
# 0110100           7
# 0110101           8
# 1110101           9
# 0000111
# 0100000
# 0111110
# 0111000


import sys
from collections import deque


num = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(num):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

result = []


def bfs(x: int, y: int) -> int:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    count = 1
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= num or ny < 0 or ny >= num or graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


for i in range(num):
    for j in range(num):
        if graph[i][j] == 1:
            result.append(bfs(i, j))


print(len(result))
for i in sorted(result):
    print(i)

