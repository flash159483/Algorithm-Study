# 1306. Jump Game III
# Medium

# Given an array of non-negative integers arr, you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
#
# Notice that you can not jump outside of the array at any time.


# Example
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        q = collections.deque([start])
        visited = [False] * len(arr)
        visited[start] = True
        while q:
            cur = q.popleft()

            for n in (cur - arr[cur], cur + arr[cur]):
                if 0 <= n < len(arr) and not visited[n]:
                    if arr[n] == 0:
                        return True

                    visited[n] = True
                    q.append(n)