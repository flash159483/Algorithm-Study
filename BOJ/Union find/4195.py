# 4195
# gold 2

# 민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.
#
# 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
#
# 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

# Example:
# Input             output
# 2                 2
# 3                 3
# Fred Barney       4
# Barney Betty      2
# Betty Wilma       2
# 3                 4
# Fred Barney
# Betty Wilma
# Barney Betty

import sys
import collections

input = sys.stdin.readline


def find(n1):
    while n1 != people[n1]:
        n1 = people[n1]
        people[n1] = people[people[n1]]
    return n1


def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return
    if level[p1] >= level[p2]:
        people[p2] = p1
        level[p1] += level[p2]
    else:
        people[p1] = p2
        level[p2] += level[p1]


for _ in range(int(input())):
    people = collections.defaultdict(str)
    level = collections.defaultdict(int)
    n = int(input())
    for i in range(n):
        a, b = input().rstrip().split()
        if a not in people:
            people[a] = a
            level[a] = 1
        if b not in people:
            people[b] = b
            level[b] = 1
        union(a, b)
        print(level[find(a)])