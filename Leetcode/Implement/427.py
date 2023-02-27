# 427. Construct Quad Tree
# Medium

# Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.
#
# Return the root of the Quad-Tree representing the grid.
#
# Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

# Example
# Input: grid = [[0,1],[1,0]]
# Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
# Explanation: The explanation of this example is shown below:
# Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None

        flag = True
        first = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if first != grid[i][j]:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            return Node(grid[0][0] == 1, True, None, None, None, None)

        else:
            n = len(grid)
            return Node('*',
                        False,
                        self.construct([r[:n // 2] for r in grid[:n // 2]]),
                        self.construct([r[n // 2:] for r in grid[:n // 2]]),
                        self.construct([r[:n // 2] for r in grid[n // 2:]]),
                        self.construct([r[n // 2:] for r in grid[n // 2:]]))