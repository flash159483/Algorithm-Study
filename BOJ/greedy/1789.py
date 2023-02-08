# 1789
# silver 5

# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?


# Example
# input         output
# 200           19

s = int(input())
addup = 0

num = 1
while addup != s:
    if addup + num < s:
        addup += num
    elif addup + num > s:
        num -= 1
        break
    else:
        break
    num += 1

print(num)