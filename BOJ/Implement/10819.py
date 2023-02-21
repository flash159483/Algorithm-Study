# 10819
# Silver 2

# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
#
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# example
# Input             Output
# 6
# 20 1 15 8 4 10    62
import itertools

n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in list(itertools.permutations(arr)):
    tmp = 0
    for j in range(n-1):
        tmp += abs(i[j] - i[j+1])

    result = max(result, tmp)

print(result)