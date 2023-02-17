# 872. Leaf-Similar Trees
# Easy

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


# Example
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def bfs(root):
            q = []
            q.append(root)
            leaf = []
            while q:
                cur = q.pop()
                print(cur.val)
                if not cur.left and not cur.right:
                    leaf.append(cur.val)
                    continue
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            return leaf

        return bfs(root1) == bfs(root2)
