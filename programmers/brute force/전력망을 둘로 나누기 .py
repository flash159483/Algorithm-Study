# 전력망을 둘로 나누기
# Level 2

# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.
#
# 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

import collections


def bfs(graph, visited, start):
    q = collections.deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


def solution(n, wires):
    result = float('inf')
    for i in range(len(wires)):
        g = wires[:i] + wires[i + 1:]
        graph = collections.defaultdict(list)
        for a, b in g:
            graph[a].append(b)
            graph[b].append(a)

        connect = set()
        for i in range(1, n + 1):
            visited = [False] * (n + 1)
            bfs(graph, visited, i)
            connect.add(visited.count(True))
        result = min(result, max(connect) - min(connect))
    return result