# 1929
# silver 3

# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# Example
# Input:
# 3 16
# output
# 3
# 5
# 7
# 11
# 13

from math import sqrt


def find_prime(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


l, h = map(int, input().split())


result = 0

for i in range(l, h+1):
    if find_prime(i):
        print(i)