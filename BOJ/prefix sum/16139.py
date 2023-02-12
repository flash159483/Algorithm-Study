# 16139
# silver 1

# 승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다.
#
# '문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'

# Example
# Input                     Output
# seungjaehwang             0
# 4                         1
# a 0 5                     2
# a 0 6                     1
# a 6 10
# a 7 10

import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())
arr = [[0] * 26 for i in range(len(name))]

arr[0][ord(name[0]) - 97] = 1

for i in range(1, len(name)):
    arr[i][ord(name[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]

for i in range(n):
    word, *a = input().split()
    if int(a[0]) > 0:
        result = arr[int(a[1])][ord(word) - 97] - arr[int(a[0]) - 1][ord(word) - 97]
    else:
        result = arr[int(a[1])][ord(word) - 97]
    print(result)
