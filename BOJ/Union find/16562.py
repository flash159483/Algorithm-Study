# 16562
# Gold 4

# 19학번 이준석은 학생이 N명인 학교에 입학을 했다. 준석이는 입학을 맞아 모든 학생과 친구가 되고 싶어한다. 하지만 준석이는 평생 컴퓨터랑만 대화를 하며 살아왔기 때문에 사람과 말을 하는 법을 모른다.
# 그런 준석이에게도 희망이 있다. 바로 친구비다!
#
# 학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다! 준석이에게는 총 k원의 돈이 있고 그 돈을 이용해서 친구를 사귀기로 했다. 막상 친구를 사귀다 보면 돈이 부족해질 것 같다는 생각을 하게 되었다.
# 그래서 준석이는 “친구의 친구는 친구다”를 이용하기로 했다.
#
# 준석이는 이제 모든 친구에게 돈을 주지 않아도 된다!
#
# 위와 같은 논리를 사용했을 때, 가장 적은 비용으로 모든 사람과 친구가 되는 방법을 구하라.

# Example
# Input             Output
# 5 3 20            20
# 10 10 20 20 30
# 1 3
# 2 4
# 5 4

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
money = list(map(int ,input().split()))
par = [i for i in range(n+1)]


def find(n):
    while n != par[n]:
        n = par[n]
        par[n] = par[par[n]]

    return n


def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return
    else:
        if money[p1-1] < money[p2-1]:
            par[p2] = p1
        else:
            par[p1] = p2

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

result = 0
pay = set()
for i in range(1, n+1):
    a = find(i)
    if a in pay:
        continue
    else:
        result += money[a-1]
        pay.add(a)

if result > k:
    print('Oh no')
else:
    print(result)