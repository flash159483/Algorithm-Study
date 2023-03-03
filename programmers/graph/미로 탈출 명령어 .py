# 미로 탈출 명령어
# Level 3

# n x m 격자 미로가 주어집니다. 당신은 미로의 (x, y)에서 출발해 (r, c)로 이동해서 탈출해야 합니다.
#
# 단, 미로를 탈출하는 조건이 세 가지 있습니다.
#
# 격자의 바깥으로는 나갈 수 없습니다.
# (x, y)에서 (r, c)까지 이동하는 거리가 총 k여야 합니다. 이때, (x, y)와 (r, c)격자를 포함해, 같은 격자를 두 번 이상 방문해도 됩니다.
# 미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 합니다.
# 이동 경로는 다음과 같이 문자열로 바꿀 수 있습니다.
#
# l: 왼쪽으로 한 칸 이동
# r: 오른쪽으로 한 칸 이동
# u: 위쪽으로 한 칸 이동
# d: 아래쪽으로 한 칸 이동
# 예를 들어, 왼쪽으로 한 칸, 위로 한 칸, 왼쪽으로 한 칸 움직였다면, 문자열 "lul"로 나타낼 수 있습니다.
#
# 미로에서는 인접한 상, 하, 좌, 우 격자로 한 칸씩 이동할 수 있습니다.


def solution(n, m, x, y, r, c, k):
    stack = [(x, y, '')]
    dir = ['u', 'r', 'l', 'd']
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    ans = 'impossible'
    while stack:
        sx, sy, path = stack.pop()
        if (sx, sy) == (r, c) and len(path) == k:
            ans = path
            break

        left = k - len(path)
        dist_remain = abs(sx - r) + abs(sy - c)

        if left < dist_remain or left % 2 != dist_remain % 2:
            continue
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if 0 < nx <= n and 0 < ny <= m:
                stack.append((nx, ny, path + dir[i]))

    return ans