# 17829
# silver2

# 조기 졸업을 꿈꾸는 종욱이는 요즘 핫한 딥러닝을 공부하던 중, 이미지 처리에 흔히 쓰이는 합성곱 신경망(Convolutional Neural Network, CNN)의 풀링 연산에 영감을 받아 자신만의 풀링을 만들고 이를 222-풀링이라 부르기로 했다.
#
# 다음은 8×8 행렬이 주어졌다고 가정했을 때 222-풀링을 1회 적용하는 과정을 설명한 것이다
#
# 행렬을 2×2 정사각형으로 나눈다.
#
#
#
# 각 정사각형에서 2번째로 큰 수만 남긴다. 여기서 2번째로 큰 수란, 정사각형의 네 원소를 크기순으로 a4 ≤ a3 ≤ a2 ≤ a1 라 했을 때, 원소 a2를 뜻한다.
#
#
#
# 2번 과정에 의해 행렬의 크기가 줄어들게 된다.
#
# 종욱이는 N×N 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.
#
# 랩실 활동에 치여 삶이 사라진 종욱이를 애도하며 종욱이의 궁금증을 대신 해결해주자.

#input                      #output
# 4                         11
# -6 -8 7 -4
# -5 -5 14 11
# 11 11 -1 -1
# 4 9 -2 -4

import sys

input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]


def solve(x, y, n):
    if n == 2:
        max_val = [table[x][y], table[x+1][y], table[x][y+1], table[x+1][y+1]]
        max_val.sort()
        return max_val[-2]
    else:
        n = n // 2
        a = solve(x, y, n)
        b = solve(x, y + n, n)
        c = solve(x + n, y, n)
        d = solve(x + n, y + n, n)
        answer = [a, b, c, d]
        answer.sort()
        return answer[-2]


print(solve(0, 0, N))