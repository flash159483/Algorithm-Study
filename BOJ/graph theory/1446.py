#1446
#silver 1

# 매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다.
# 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.
#
# 세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

#example
#input                              output
# 5 150                             70
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90


import sys
import heapq


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    dist = [sys.maxsize] * (D+1)

    while q:
        weight, cur = heapq.heappop(q)
        if weight > dist[cur]:
            continue
        for i in graph[cur]:
            dw = weight + i[1]
            if dw < dist[i[0]]:
                dist[i[0]] = dw
                heapq.heappush(q, (dw, i[0]))
    return dist[D]


input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    a, b, w = map(int, input().split())
    if b > D:
        continue
    graph[a].append((b, w))

print(dijkstra())


