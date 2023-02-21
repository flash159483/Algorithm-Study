# 여행경로
# level 3

# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
#
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# example
# ["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.
import collections


def solution(tickets):
    graph = collections.defaultdict(list)
    for x, y in tickets:
        graph[x].append(y)

    for i in graph:
        graph[i].sort(reverse=True)

    stack = ['ICN']
    path = []

    while stack:
        cur = stack.pop()

        if cur not in graph or not graph[cur]:
            path.append(cur)
        else:
            stack.append(cur)
            stack.append(graph[cur].pop())

    return path[::-1]