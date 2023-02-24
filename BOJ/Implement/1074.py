# 1074
# Silver 1

# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
#
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
#
# 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.
#
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
#
# 다음은 N=3일 때의 예이다.

# Example
# Input             Output
# 2 3 1             11

import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())
n = 2 ** n
cnt = 0

result = 0


def solve(x, y, w):
    global result
    if x > r or x + w <= r or y > c or y + w <= c:
        result += w ** 2
        return

    if w > 2:
        w = w // 2
        solve(x, y, w)
        solve(x, y + w, w)
        solve(x + w, y, w)
        solve(x + w, y + w, w)
    else:
        if x == r and y == c:
            print(result)
        elif x == r and y + 1 == c:
            print(result + 1)
        elif x + 1 == r and y == c:
            print(result + 2)
        else:
            print(result + 3)
        exit()

solve(0, 0, n)

