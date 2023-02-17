# 783. Minimum Distance Between BST Nodes
# Easy

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.


# Example
# Input: root = [4,2,6,1,3]
# Output: 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.pre)
        self.pre = root.val

        self.minDiffInBST(root.right)
        return self.result
