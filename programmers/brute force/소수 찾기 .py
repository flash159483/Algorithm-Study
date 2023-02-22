# 소수 찾기
# Level 2

# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
#
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

import math
import itertools


def solution(numbers):
    def prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    result = 0
    seen = set()
    for i in range(len(numbers)):
        for num in itertools.permutations(list(numbers), i + 1):
            n = int(''.join(num))
            if prime(n) and n not in seen:
                seen.add(n)
                result += 1

    return result