# 10026
# gold 5

# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
#
# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데,
# 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
#
# 예를 들어, 그림이 아래와 같은 경우에
#
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
#
# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

# Example
#input              output
# 5                 4 3
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR


import sys
from copy import deepcopy


def dfs(i, j, color):
    if i < 0 or i >= num or j < 0 or j >= num or tmp_graph[i][j] != color:
        return

    tmp_graph[i][j] = '0'
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for n in range(4):
        nx = dx[n] + i
        ny = dy[n] + j

        dfs(nx, ny, color)


sys.setrecursionlimit(10000)

num = int(sys.stdin.readline().rstrip())
graph = []

for _ in range(num):
    graph.append(list(sys.stdin.readline().rstrip()))

result = 0
tmp_graph = deepcopy(graph)
for i in range(num):
    for j in range(num):
        if tmp_graph[i][j] != '0':
            dfs(i, j, tmp_graph[i][j])
            result += 1

print(result, end=' ')

for i in range(num):
    for j in range(num):
        if graph[i][j] == "R":
            graph[i][j] = "G"

tmp_graph = deepcopy(graph)


result = 0
for i in range(num):
    for j in range(num):
        if tmp_graph[i][j] != '0':
            dfs(i, j, tmp_graph[i][j])
            result += 1
print(result)