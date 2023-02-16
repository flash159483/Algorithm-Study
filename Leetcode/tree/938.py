# 938. Range Sum of BST
# Easy

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


# Example
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []

        def dfs(root):
            if not root:
                return
            if low <= root.val <= high:
                result.append(root.val)
            if root.val < high:
                dfs(root.right)
            if root.val > low:
                dfs(root.left)

            return

        dfs(root)
        return sum(result)