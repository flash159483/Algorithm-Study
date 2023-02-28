# 등산코스 정하기
# Level 3

# XX산은 n개의 지점으로 이루어져 있습니다. 각 지점은 1부터 n까지 번호가 붙어있으며, 출입구, 쉼터, 혹은 산봉우리입니다. 각 지점은 양방향 통행이 가능한 등산로로 연결되어 있으며, 서로 다른 지점을 이동할 때 이 등산로를 이용해야 합니다. 이때, 등산로별로 이동하는데 일정 시간이 소요됩니다.
#
# 등산코스는 방문할 지점 번호들을 순서대로 나열하여 표현할 수 있습니다.
# 예를 들어 1-2-3-2-1 으로 표현하는 등산코스는 1번지점에서 출발하여 2번, 3번, 2번, 1번 지점을 순서대로 방문한다는 뜻입니다.
# 등산코스를 따라 이동하는 중 쉼터 혹은 산봉우리를 방문할 때마다 휴식을 취할 수 있으며, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity라고 부르기로 합니다.
#
# 당신은 XX산의 출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 다시 원래의 출입구로 돌아오는 등산코스를 정하려고 합니다. 다시 말해, 등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 합니다.
# 당신은 이러한 규칙을 지키면서 intensity가 최소가 되도록 등산코스를 정하려고 합니다.
#
# 다음은 XX산의 지점과 등산로를 그림으로 표현한 예시입니다.


import collections
import heapq


def solution(n, paths, gates, summits):
    def solve():
        heap = []
        visited = [float('inf')] * (n + 1)
        for gate in gates:
            heapq.heappush(heap, (0, gate))
            visited[gate] = 0

        while heap:
            weight, cur = heapq.heappop(heap)
            if weight > visited[cur] or cur in summit:
                continue

            for ne, w in graph[cur]:
                new_weight = max(w, weight)
                if new_weight < visited[ne]:
                    visited[ne] = new_weight
                    heapq.heappush(heap, (new_weight, ne))

        ans = [0, float('inf')]
        for s in summits:
            if visited[s] < ans[1]:
                ans[1] = visited[s]
                ans[0] = s

        return ans

    graph = collections.defaultdict(list)
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    summits.sort()
    summit = set(summits)

    return solve()

