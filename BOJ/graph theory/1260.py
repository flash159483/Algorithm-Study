# 1260
# silver 2

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# Example
#input              output
#4 5 1              1 2 4 3
# 1 2               1 2 3 4
# 1 3
# 1 4
# 2 4
# 3 4


import sys
import collections
from typing import List

point, edge, start = map(int, sys.stdin.readline().rstrip().split())
graph = collections.defaultdict(list)
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node: int, discovered: List[int]) -> None:
    discovered.append(node)
    print(node, end=' ')
    for i in sorted(graph[node]):
        if i not in discovered:
            dfs(i, discovered)


def bfs(node: int) -> None:
    queue = collections.deque([start])
    discovered = [start]
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in sorted(graph[node]):
            if i not in discovered:
                discovered.append(i)
                queue.append(i)


dfs(start, [])
print()
bfs(start)

