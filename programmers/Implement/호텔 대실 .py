# 호텔 대실
# Level 2

# 호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
# 예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

# Example
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

import heapq


def clean(time):
    h, m = map(int, time.split(':'))
    m += 10
    if m >= 60:
        h += 1
        m -= 60

    return str(h).rjust(2, '0') + ':' + str(m).rjust(2, '0')


def solution(book_time):
    book_time.sort()

    room = []
    ans = 1

    for start, end in book_time:
        if not room:
            heapq.heappush(room, clean(end))
            continue
        if room[0] <= start:
            heapq.heappop(room)
        else:
            ans += 1
        heapq.heappush(room, clean(end))

    return ans