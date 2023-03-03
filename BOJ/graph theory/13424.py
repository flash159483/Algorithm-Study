# 13424
# Gold 4

# 해리와 친구들은 엄브릿지의 감시를 피해 어둠의 마법 방어술을 연습하기 위한 비밀 모임을 하려고 한다. 그들은 아무도 모르게 모임의 장소를 전달하기 위해 가짜 갈레온을 사용하는데,
# 해리가 자신의 가짜 갈레온에 모임의 장소를 적으면 친구들이 가진 가짜 갈레온에 해리가 적은 장소가 나타난다. 해리가 다니고 있는 호그와트 마법 학교에는 모임에 사용할만한 N개의 방이 있다.
# 각 방에는 1부터 N까지 번호가 붙어 있으며 중복된 번호는 없다. 마법 학교답게 N개의 방은 M개의 마법으로 만들어진 비밀통로로 연결되어있다. 모든 비밀통로는 양방향 통행이 가능하며 자연수의 길이를 가진다. 모임에 참여하는 친구들은 총 K명이다.
#
# 해리는 N개의 방 중에서 한 곳을 정해 오늘 모임의 장소로 이용하려고 한다. 모임 장소를 정하기 전, 호그와트 비밀지도를 이용해 학교 안에 있는 사람들의 현재 위치를 확인해보니 모임에 참여하는 친구들은 N개의 방 중에서 한군데씩에 각각 위치해 있었다.
# 불행하게도 호그와트 안에서는 순간이동이 금지되어 있어서 모임에 참여하는 친구들은 들키지 않도록 비밀통로만 이용해서 오늘의 모임 장소로 가려고 한다.
# 이때 이들은 항상 처음 위치에서 모임 장소까지의 이동 거리가 가장 짧은 경로만을 이용한다. 여기서 ‘이동 거리’란 처음 위치에서 모임 장소까지 가기 위해 이용한 비밀 통로들의 길이의 합을 의미한다.
# 어느 방을 모임 장소로 사용할까 고민하던 해리는 모임에 참석하는 친구들의 이동 거리의 총합이 최소가 되는 방을 오늘의 모임 장소로 사용하기로 했다. 다음 그림은 N = 6, M = 7, K = 2인 경우의 예시이다.

# Example
# Input             Output
# 2                 1
# 6 7               2
# 1 2 4
# 1 3 1
# 1 5 2
# 2 3 2
# 3 4 3
# 4 5 2
# 6 5 1
# 2
# 3 5
# 4 5
# 1 2 2
# 1 3 1
# 2 3 2
# 2 4 3
# 3 4 6
# 2
# 3 4

import sys
import collections
import heapq

input = sys.stdin.readline


def dijsktra(start):
    q = []

    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        weight ,now = heapq.heappop(q)
        if weight > dist[now]:
            continue
        for i in graph[now]:
            cost = weight + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = collections.defaultdict(list)

    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    f = int(input())
    friends = list(map(int, input().split()))
    arr = [0] * (n+1)
    for friend in friends:
        dist = [sys.maxsize] * (n + 1)
        dijsktra(friend)
        for i in range(1, n + 1):
            arr[i] += dist[i]

    ans = 0
    now = sys.maxsize

    for i in range(1, n+1):
        if now > arr[i]:
            now = arr[i]
            ans = i

    print(ans)