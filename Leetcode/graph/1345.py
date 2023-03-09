# 1345. Jump Game IV
# Hard

# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.

# Example
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        adj = defaultdict(list)
        for i, n in enumerate(arr):
            adj[n].append(i)

        ans = [0] * len(arr)
        q = collections.deque([len(arr) - 1])

        while q:
            i = q.popleft()
            if i < len(arr) - 2 and ans[i + 1] == 0:
                ans[i + 1] = ans[i] + 1
                q.append(i + 1)
            if i > 0 and ans[i - 1] == 0:
                ans[i - 1] = ans[i] + 1
                if i - 1 == 0:
                    return ans[0]
                q.append(i - 1)

            for j in adj[arr[i]]:
                if ans[j] == 0 and j < len(arr) - 1:
                    ans[j] = ans[i] + 1
                    if j == 0:
                        return ans[0]
                    q.append(j)
            adj.pop(arr[i])
