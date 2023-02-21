# 아이템 줍기
# level 3

# 지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때,
# 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.


import collections


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[5] * 102 for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    q = collections.deque()
    q.append((characterX * 2, characterY * 2, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, c = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            return c // 2
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102 and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny, c + 1))
