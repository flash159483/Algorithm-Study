# 11000
# Gold 5

# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
#
# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
#
# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
#
# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

# Example
# Input:            output:
# 3                 2
# 1 3
# 2 4
# 3 5


import sys
import heapq

input = sys.stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort()

ongoing = [classes[0][1]]

for c in classes[1:]:
    if c[0] >= ongoing[0]:
        heapq.heappop(ongoing)
    heapq.heappush(ongoing, c[1])

print(len(ongoing))