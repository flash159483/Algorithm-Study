# 24060
# silver 4

# 오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.
#
# 크기가 N인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.

# Example
# Input                 Output
# 5 7                   3
# 4 5 1 3 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    tmp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            result.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            result.append(right[j])
            j += 1

    while i < len(left):
        tmp.append(left[i])
        result.append(left[i])
        i += 1

    while j < len(right):
        tmp.append(right[j])
        result.append(right[j])
        j += 1

    return tmp


merge_sort(arr)
if len(result) >= m:
    print(result[m - 1])
else:
    print(-1)
