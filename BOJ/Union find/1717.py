# 1717
# gold 4

# 초기에
# $n+1$개의 집합
# $\{0\}, \{1\}, \{2\}, \dots , \{n\}$이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

# 집합을 표현하는 프로그램을 작성하시오.

# Example:
# Input             output
# 7 8               NO
# 0 1 3             NO
# 1 1 7             YES
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

par = [i for i in range(n + 1)]


def find(cur):
    while par[cur] != cur:
        cur = par[cur]
        par[cur] = par[par[cur]]

    return cur


def union(n1, n2):
    p1, p2 = find(n1), find(n2)

    if p1 == p2:
        return
    else:
        par[p1] = p2


for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')