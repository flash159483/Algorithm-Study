# 주차 요금 계산
# Level 2

# 주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.
#
# 요금표
# 기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
# 180	5000	10	600
#
#
# 입/출차 기록
# 시각(시:분)	차량 번호	내역
# 05:34	5961	입차
# 06:00	0000	입차
# 06:34	0000	출차
# 07:59	5961	출차
# 07:59	0148	입차
# 18:59	0000	입차
# 19:09	0148	출차
# 22:59	5961	입차
# 23:00	5961	출차


import collections
from math import ceil


def hourtomin(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m


def solution(fees, records):
    time = {}
    cars = collections.defaultdict(int)
    for r in records:
        t, num, _ = r.split()
        if num in time:
            first = time[num]
            del time[num]
            cars[num] += hourtomin(t) - hourtomin(first)
        else:
            time[num] = t

    for left in time:
        cars[left] += hourtomin('23:59') - hourtomin(time[left])
    result = []
    car = list(cars.keys())
    car.sort()
    for c in car:
        if cars[c] > fees[0]:
            result.append(fees[1] + ceil((cars[c] - fees[0]) / fees[2]) * fees[3])
        else:
            result.append(fees[1])

    return result

