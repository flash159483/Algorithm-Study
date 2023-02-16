# 11657
# gold 4

# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시,
# C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.
#
# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.


# Example
# Input         Output
# 3 4           4
# 1 2 4         3
# 1 3 3
# 2 3 -1
# 3 1 -2


import sys

input = sys.stdin.readline


def bellman_ford():
    dist[1] = 0

    for i in range(n):
        for j in range(e):
            start, nex, cost = graph[j][0], graph[j][1], graph[j][2]
            if dist[start] != sys.maxsize and dist[nex] > dist[start] + cost:
                dist[nex] = dist[start] + cost
                if i == n - 1:
                    return True
    return False


n, e = map(int, input().split())
graph = []
dist = [sys.maxsize] * (n + 1)
for _ in range(e):
    a, b, w = map(int, input().split())
    graph.append((a, b, w))

cycle = bellman_ford()

if cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == sys.maxsize:
            print(-1)
        else:
            print(dist[i])
