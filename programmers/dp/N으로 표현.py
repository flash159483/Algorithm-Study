# N으로 표현
# Level 3

# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
#
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
def solution(N, number):
    res_list = []

    for cnt in range(1, 9):
        tmp = set()
        tmp.add(int(str(N) * cnt))
        for i in range(cnt - 1):
            for first in res_list[i]:
                for second in res_list[-i - 1]:
                    tmp.add(first + second)
                    tmp.add(first - second)
                    tmp.add(first * second)
                    if second:
                        tmp.add(first // second)
        if number in tmp:
            return cnt
        res_list.append(tmp)

    return -1