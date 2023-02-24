# 5525
# Silver 1

# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
#
# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

# Example
# Input             Output
# 1                 4
# 13
# OOIOIOIOIIOII


import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = input().rstrip()

target = 'IO'*n + 'I'

result = cnt = 0
i = 0
while i < (m - 1):
    if arr[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(result)