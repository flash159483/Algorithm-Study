# 11404
# gold 4

# n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.
#
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

#Example
#Input                  Output
# 5                     0 2 3 1 4
# 14                    12 0 15 2 5
# 1 2 2                 8 5 0 1 1
# 1 3 3                 10 7 13 0 3
# 1 4 1                 7 4 10 6 0
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

matrix = [[sys.maxsize]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a][b] = min(c, matrix[a][b])


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if matrix[i][j] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(matrix[i][j], end = ' ')
    print()