# 7453
# gold 2

# 정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.
#
# A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.


# Example
#input              output
# 6                 5
# -45 22 42 -16
# -41 -27 56 30
# -36 53 -37 77
# -36 30 -75 -46
# 26 -38 -10 62
# -32 -54 -6 45

import sys

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())

    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = {}
for i in A:
    for j in B:
        if not ab.get(i+j):
            ab[i+j] = 1
        else:
            ab[i+j] += 1

result = 0

for i in C:
    for j in D:
        result += ab.get(-(i+j), 0)

print(result)