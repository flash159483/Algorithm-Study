# 1738
# Gold 2

# 민승이는 놀러가기 위해 집을 나섰다. 민승이네 집에서 코레스코 콘도까지 가기 위해서는 복잡하게 얽혀있는 골목길들을 통과해야 한다.
#
# 그런데, 어떤 길에는 깡패가 서식하고 있어, 그 길을 지나게 되면 깡패에게 일정한 양의 금품을 갈취당하게 된다. 그런가하면, 어떤 길에는 지나가던 행인들이 흘리고 간 금품들이 떨어져 있어, 그 길을 지나게 되면 일정한 양의 금품을 획득하게 된다. 한 번 지나간 길을 다시 방문하더라도 금품을 갈취당하거나 획득한다.
#
# 골목길의 연결 상태와, 각 골목길을 지날 때 갈취당하거나 획득하게 되는 금품의 양이 주어졌을 때, 민승이가 최대한 유리한 경로를 따라 집에서 코레스코 콘도까지 가기 위해서는 어떻게 해야 하는지 출력하는 프로그램을 작성하시오.
#
# 보유 중인 금품의 양이 음수가 될 수 있다. 최대한 유리한 경로 또는 최적의 경로는 민승이네 집에서 출발하여 코레스코 콘도에 도착하는 경로 중 금품의 양이 최대가 되는 경로이다.

# Example
# Input             Output
# 5 7               1 2 3 4 5
# 1 2 3
# 1 3 4
# 3 1 -7
# 2 3 2
# 3 4 1
# 4 2 -5
# 4 5 1

import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
graph = collections.defaultdict(list)
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
path = [0] * (n + 1)
def bellman_ford():
    dist = [-sys.maxsize] * (n + 1)
    dist[1] = 0
    for i in range(n):
        for cur in range(1, n + 1):
            for nex, weight in graph[cur]:
                if dist[cur] != -sys.maxsize and dist[nex] < dist[cur] + weight:
                    dist[nex] = dist[cur] + weight
                    path[nex] = cur
                    if i == n - 1:
                        dist[nex] = sys.maxsize

    if dist[n] == sys.maxsize:
        print(-1)
    else:
        cur = n
        result = []
        while cur != 1:
            result.append(cur)
            cur = path[cur]
        result.append(cur)
        print(*result[::-1])

bellman_ford()