# 226. Invert Binary Tree
# Easy

# Given the root of a binary tree, invert the tree, and return its root.

# Example
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        #top-down method
        while queue:
            #to use dfs just need to use stack instead of queue
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
        return root

        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        #     return root
        # return None
