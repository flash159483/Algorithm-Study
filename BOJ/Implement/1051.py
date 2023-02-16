# 1051
# Silver 4

# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.


# Example
# Input             Output
# 3 5               9
# 42101
# 22100
# 22101


import sys

input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
w = min(n, m)
result = 0
while w != 0:
    for i in range(n - w + 1):
        for j in range(m - w + 1):
            if len({graph[i][j], graph[i][j + w - 1], graph[i + w - 1][j], graph[i + w - 1][j + w - 1]}) == 1:
                result = max(result, w ** 2)

    w -= 1

print(result)