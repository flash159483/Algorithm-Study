# 두 큐 합 같게 만들기
# level 2

# 길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다.
# 이때 필요한 작업의 최소 횟수를 구하고자 합니다. 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.
#
# 큐는 먼저 집어넣은 원소가 먼저 나오는 구조입니다. 이 문제에서는 큐를 배열로 표현하며, 원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다. 즉, pop을 하면 배열의 첫 번째 원소가 추출되며,
# insert를 하면 배열의 끝에 원소가 추가됩니다. 예를 들어 큐 [1, 2, 3, 4]가 주어졌을 때, pop을 하면 맨 앞에 있는 원소 1이 추출되어 [2, 3, 4]가 되며, 이어서 5를 insert하면 [2, 3, 4, 5]가 됩니다.

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    limit = len(q1) * 4
    s1 = sum(queue1)
    s2 = sum(queue2)
    while True:
        if s1 < s2:
            tmp = q2.popleft()
            s2 -= tmp
            s1 += tmp
            q1.append(tmp)
        elif s1 > s2:
            tmp = q1.popleft()
            s1 -= tmp
            s2 += tmp
            q2.append(tmp)
        else:
            return cnt
        cnt += 1
        if cnt == limit:
            return -1



