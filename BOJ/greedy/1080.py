# 1080
# silver 1

# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)


# Example
# input         output
# 3 4           2
# 0000
# 0010
# 0000
# 1001
# 1011
# 1001

def rev(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix_a[i][j] = 1 - matrix_a[i][j]


def check():
    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False

    return True


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix_a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
matrix_b = [list(map(int, list(input().rstrip()))) for _ in range(n)]
result = 0

for i in range(n - 2):
    for j in range(m - 2):
        if matrix_a[i][j] != matrix_b[i][j]:
            rev(i, j)
            result += 1

print(result if check() else -1)