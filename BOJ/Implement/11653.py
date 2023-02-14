# 11653
# bronze 1

# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
# Example
# Input                 Output
# 72                    2
#                       2
#                       2
#                       3
#                       3

n = int(input())

d = 2
while n != 1:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 1
