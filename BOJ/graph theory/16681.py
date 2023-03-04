# 16681
# Gold 2

# 주환이는 요즘 등산에 빠졌다. 주환이는 등산을 위해 지도를 가지고 있는데, 그 지도에는 각 지점의 높이와 갈 수 있는 다른 지점까지의 거리가 표시되어 있다.
#
# 주환이는 아침에 집에서 출발하여 등산을 갔다가, 오후 수업을 듣기 위해 고려대학교로 돌아와야 한다.
#
# 주환이는 지도의 임의의 지점을 골라, 그 지점을 목표로 정한다. 집 또는 고려대학교는 목표로 선택할 수 없다.
# 주환이가 집에서 정한 목표에 도달할 때 까지는 항상 높이가 증가하는 방향으로만 이동해야 한다.
# 주환이가 정한 목표에 도달한 후, 고려대학교로 갈 때에는 항상 높이가 감소하는 방향으로만 이동해야 한다.
# 주환이는 거리 1을 움직일 때 마다 D 의 체력이 소모된다.
# 주환이는 정한 목표에 도달하면 높이 1당 E 의 성취감을 얻는다. 즉 높이가 h인 목표에 도달하면 hE의 성취감을 얻는다.
# 주환이는 이 등산의 가치를 (얻은 성취감) - (소모한 체력) 으로 계산하기로 하였다. 주환이를 위해 가치가 가장 높은 등산 경로를 선택해주자.

# Example
# Input             Output
# 8 13 4 9          15
# 1 4 7 3 10 2 15 1
# 1 2 3
# 3 4 2
# 5 6 6
# 7 8 2
# 2 3 4
# 6 7 2
# 3 6 1
# 4 8 3
# 5 1 6
# 8 3 5
# 2 5 4
# 4 6 3
# 5 3 8

import sys
import heapq
import collections

input = sys.stdin.readline

def dijkstra(start):
    dist = [sys.maxsize] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        weight, cur = heapq.heappop(q)
        if dist[cur] < weight:
            continue
        for v, w in graph[cur]:
            if arr[v] > arr[cur]:
                dw = w + weight
                if dist[v] > dw:
                    dist[v] = dw
                    heapq.heappush(q, (dw, v))
    return dist


n, m, d, e = map(int, input().split())
arr = [-1] + list(map(int, input().split()))
graph = collections.defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

res1 = dijkstra(1)
res2 = dijkstra(n)
ans = []
for i in range(1, n + 1):
    if res1[i] != sys.maxsize and res2[i] != sys.maxsize:
        ans.append(arr[i] * e - d * (res1[i] + res2[i]))

print(max(ans) if ans else 'Impossible')
