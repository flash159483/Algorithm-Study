# 1629
# Silver 1

# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

# Example
# Input         Output
# 10 11 12      4

n, m, k = map(int, input().split())


def solve(m):
    if m == 1:
        return n % k
    else:
        tmp = solve(m // 2)
        if m % 2 == 0:
            return (tmp * tmp) % k
        else:
            return (tmp * tmp * n) % k


print(solve(m))
