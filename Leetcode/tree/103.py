# 103. Binary Tree Zigzag Level Order Traversal
# Medium

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])

        result = [[root.val]]
        zigzag = True
        while q:
            tmp = []
            for i in range(len(q)):
                cur = q.popleft()
                if not cur:
                    continue
                q.append(cur.left)
                q.append(cur.right)
                if cur.left:
                    tmp.append(cur.left.val)
                if cur.right:
                    tmp.append(cur.right.val)
            if tmp and zigzag:
                result.append(reversed(tmp))
                zigzag = False
            elif tmp and not zigzag:
                result.append(tmp)
                zigzag = True

        return result