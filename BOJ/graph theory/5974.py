# 5972
# gold 5

# 농부 현서는 농부 찬홍이에게 택배를 배달해줘야 합니다. 그리고 지금, 갈 준비를 하고 있습니다. 평화롭게 가려면 가는 길에 만나는 모든 소들에게 맛있는 여물을 줘야 합니다.
# 물론 현서는 구두쇠라서 최소한의 소들을 만나면서 지나가고 싶습니다.
#
# 농부 현서에게는 지도가 있습니다. N (1 <= N <= 50,000) 개의 헛간과, 소들의 길인 M (1 <= M <= 50,000) 개의 양방향 길이 그려져 있고, 각각의 길은 C_i (0 <= C_i <= 1,000) 마리의 소가 있습니다.
# 소들의 길은 두 개의 떨어진 헛간인 A_i 와 B_i (1 <= A_i <= N; 1 <= B_i <= N; A_i != B_i)를 잇습니다. 두 개의 헛간은 하나 이상의 길로 연결되어 있을 수도 있습니다.
# 농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N에 있습니다.

# Example
# Input             Output
# 6 8               5
# 4 5 3
# 2 4 0
# 4 1 4
# 2 1 1
# 5 6 1
# 3 6 2
# 3 2 6
# 3 4 4

import collections
import heapq
import sys

input = sys.stdin.readline


def dijkstra():
    dist = [sys.maxsize] * (n + 1)
    q = [(0, 1)]
    while q:
        weight, cur = heapq.heappop(q)
        if weight > dist[cur]:
            continue
        for v, w in graph[cur]:
            dw = w + weight
            if dw < dist[v]:
                dist[v] = dw
                heapq.heappush(q, (dw, v))

    return dist[n]


n, m = map(int, input().split())

graph = collections.defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra())