# 미로 탈출
# Level 2

# 1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다. 각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다.
# 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다. 레버 또한 통로들 중 한 칸에 있습니다. 따라서,
# 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다. 이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다.
# 미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.
#
# 미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요. 만약, 탈출할 수 없다면 -1을 return 해주세요.


import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    n, m = len(maps), len(maps[0])

    def bfs(x, y):
        q = collections.deque()
        q.append((x, y))
        visited = [[-1] * m for _ in range(n)]
        visited[x][y] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

        return visited

    sx = sy = 0
    lx = ly = 0
    ex = ey = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                lx, ly = i, j
            elif maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j

    ans = 0
    tmp = bfs(sx, sy)
    if tmp[lx][ly] == -1:
        return -1
    ans += tmp[lx][ly]
    tmp = bfs(lx, ly)
    if tmp[ex][ey] == -1:
        return -1
    ans += tmp[ex][ey]

    return ans