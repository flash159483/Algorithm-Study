# 1753
# gold 4

# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
# Example
#input              output
# 5 6               0
# 1                 2
# 5 1 1             3
# 1 2 2             7
# 1 3 3             INF
# 2 3 4
# 2 4 5
# 3 4 6


import sys
import collections
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())


graph = collections.defaultdict(list)
for _ in range(e):
    a, b, z = map(int, input().split())
    graph[a].append((b, z))

q = [(0, start)]

visited = [float('inf')] * (v + 1)
visited[start] = 0

while q:
    dist, cur = heapq.heappop(q)
    if visited[cur] >= dist:
        for end, w in graph[cur]:
            next_node = dist + w
            if next_node < visited[end]:
                heapq.heappush(q, (dist+w, end))
                visited[end] = next_node

for i in visited[1:]:
    print(i if i != float('inf') else "INF")
