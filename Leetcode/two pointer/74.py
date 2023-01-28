#74 Search a 2D Matrix
# Medium

# You are given an m x n integer matrix matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.

#Example
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            row += 1

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row - 1][mid] == target:
                return True

            elif matrix[row - 1][mid] < target:
                left += 1
            else:
                right -= 1

        return False
