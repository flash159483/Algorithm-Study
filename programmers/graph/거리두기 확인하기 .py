# 거리두기 확인하기
# Level 2

# 개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.
#
# 코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
# 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.
#
# 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
# 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

import collections


def solution(places):
    def bfs():
        for now in start:
            visited = [[False] * 5 for _ in range(5)]
            visited[now[0]][now[1]] = True
            q = collections.deque()
            q.append(now)
            while q:
                x, y, k = q.popleft()
                if k == 2:
                    continue

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != 'X':
                        if place[nx][ny] == 'P':
                            return 0
                        q.append((nx, ny, k + 1))
                        visited[nx][ny] = True

        return 1

    ans = []
    for place in places:
        start = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    start.append((i, j, 0))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        ans.append(bfs())
    return ans