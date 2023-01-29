#1780
#silver 2

# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
#
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

#example
#input                              output
# 9                                 10
# 0 0 0 1 1 1 -1 -1 -1              12
# 0 0 0 1 1 1 -1 -1 -1              11
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1

import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [0] * 3


def solve(x, y, n):
    first = matrix[x][y]
    flag = False
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != matrix[i][j]:
                flag = True
                break

    if flag:
        n = n // 3
        for i in range(3):
            for j in range(3):
                solve(x + n * i, y + n * j, n)
    else:
        result[first] += 1


solve(0, 0, N)
print(result[-1])
print(result[0])
print(result[1])