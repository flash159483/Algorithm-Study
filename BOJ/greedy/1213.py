# 1213
# silver 3

# 임한수와 임문빈은 서로 사랑하는 사이이다.
#
# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
#
# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
#
# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

# Example
# Input                 output
# ABACABA               AABCBAA

import collections
import sys

input = sys.stdin.readline

words = list(input().rstrip())
words.sort()

c = collections.Counter(words)

odd = 0
mid = ''
for i in c:
    if c[i] % 2 != 0:
        odd += 1
        mid += i
        words.remove(i)
        if odd > 1:
            print("I'm Sorry Hansoo")
            break

if odd <= 1:
    left = ''

    for i in range(0, len(words), 2):
        left += words[i]

    print(left + mid + left[::-1])