# 652. Find Duplicate Subtrees
# Medium

# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with the same node values.
#
#

# Example
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def solve(node):
            if not node:
                return 'null'

            tmp = "%s,%s,%s" % (str(node.val), solve(node.left), solve(node.right))
            result[tmp].append(node)

            return tmp

        result = collections.defaultdict(list)
        solve(root)

        return [result[node][0] for node in result if len(result[node]) > 1]


