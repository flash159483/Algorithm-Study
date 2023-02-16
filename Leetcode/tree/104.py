# 104. Maximum Depth of Binary Tree
# Easy

# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example
# Input: root = [3,9,20,null,null,15,7]
# Output: 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS method
        # if not root:
        #     return 0
        # queue = collections.deque([root])
        # depth = 0

        # while queue:
        #     depth += 1
        #     for _ in range(len(queue)):
        #         cur_root = queue.popleft()

        #         #check right and left of the root
        #         if cur_root.left:
        #             queue.append(cur_root.left)

        #         if cur_root.right:
        #             queue.append(cur_root.right)

        # return depth

        # DFS method
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1

        return dfs(root)