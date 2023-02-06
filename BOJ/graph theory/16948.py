# 16948
# silver 1

# 게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
#
# 크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.
#
# 데스 나이트는 체스판 밖으로 벗어날 수 없다.


# Example
# input                    output
# 7                        4
# 6 6 0 1


import collections

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q = collections.deque()
q.append((r1, c1))

visited = [[-1]*n for _ in range(n)]
visited[r1][c1] = 0
while q:
    x, y = q.popleft()

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

print(visited[r2][c2])
