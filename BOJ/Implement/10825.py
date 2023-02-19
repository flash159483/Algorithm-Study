# 10825
# silver 4

# 도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
#
# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)


# Example:
# input
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# output
# Donghyuk
# Sangkeun
# Sunyoung
# nsj
# Wonseob
# Sanghyun
# Sei
# Kangsoo
# Haebin
# Junkyu
# Soong
# Taewhan

import sys

input = sys.stdin.readline

arr = []
for i in range(int(input())):
    name, *num = input().rstrip().split()
    n = list(map(int, num))
    n += [name]
    arr.append(n)


arr.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))
for i in range(len(arr)):
    print(arr[i][3])