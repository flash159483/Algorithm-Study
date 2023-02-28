# 파괴되지 않은 건물
# Level 3

# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]
#
# N x M 크기의 행렬 모양의 게임 맵이 있습니다. 이 맵에는 내구도를 가진 건물이 각 칸마다 하나씩 있습니다. 적은 이 건물들을 공격하여 파괴하려고 합니다. 건물은 적의 공격을 받으면 내구도가 감소하고 내구도가 0이하가 되면 파괴됩니다. 반대로, 아군은 회복 스킬을 사용하여 건물들의 내구도를 높이려고 합니다.
#
# 적의 공격과 아군의 회복 스킬은 항상 직사각형 모양입니다.


def solution(board, skill):
    n = len(board)
    m = len(board[0])
    tmp = [[0] * (m + 1) for _ in range(n + 1)]
    for s in skill:
        type, x1, y1, x2, y2, d = s
        if type == 1:
            d = -d
        tmp[x1][y1] += d
        tmp[x1][y2 + 1] += -d
        tmp[x2 + 1][y1] += -d
        tmp[x2 + 1][y2 + 1] += d

    for i in range(n):
        for j in range(m):
            tmp[i][j + 1] += tmp[i][j]

    for i in range(n):
        for j in range(m):
            tmp[i + 1][j] += tmp[i][j]

    ans = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                ans += 1
    return ans

