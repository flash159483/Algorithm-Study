# 3085
# Silver 2

# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
#
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

# example
# Input             Output
# 5                 4
# YCPZY
# CYZZP
# CCPPP
# YCYZC
# CPPZZ

import sys

input = sys.stdin.readline

n = int(input())
candy = [list(input().rstrip()) for _ in range(n)]


def check_row(x, y):
    l = max(n - y, y)
    cnt = 1
    n1, n2 = y - 1, y + 1
    for i in range(l):
        if n1 >= 0:
            if candy[x][n1] == candy[x][y]:
                cnt += 1
                n1 -= 1
            else:
                n1 = -1

        if n2 < n:
            if candy[x][n2] == candy[x][y]:
                cnt += 1
                n2 += 1
            else:
                n2 = n
    return cnt


def check_col(x, y):
    l = max(n - x, x)
    cnt = 1
    n1, n2 = x - 1, x + 1
    for i in range(l):
        if n1 >= 0:
            if candy[n1][y] == candy[x][y]:
                cnt += 1
                n1 -= 1
            else:
                n1 = -1

        if n2 < n:
            if candy[n2][y] == candy[x][y]:
                cnt += 1
                n2 += 1
            else:
                n2 = n
    return cnt


result = 0
for i in range(n):
    for j in range(n - 1):
        candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        result = max(result, check_row(i, j), check_row(i, j + 1), check_col(i, j), check_col(i, j + 1))
        candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

for i in range(n- 1):
    for j in range(n):
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        result = max(result, check_row(i+1, j), check_row(i, j), check_col(i+1, j), check_col(i, j))
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(result)
