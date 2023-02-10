# 24479
# silver 2

# 오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.
#
# 깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

# Example
# Input                 output
# 5 5 1                 1
# 1 4                   2
# 1 2                   3
# 2 3                   4
# 2 4                   0
# 3 4

import sys
import collections
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
c = 1


def dfs(cur):
    global c
    visited[cur] = c
    for i in sorted(graph[cur]):
        if visited[i] == 0:
            c += 1
            dfs(i)


v, e, start = map(int, input().split())
graph = collections.defaultdict(list)

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (v+1)

dfs(start)

for i in range(1, v+1):
    print(visited[i])