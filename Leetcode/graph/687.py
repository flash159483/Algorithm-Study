# 687. Longest Univalue Path
# Medium

# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.
#
# The length of the path between two nodes is represented by the number of edges between them.

# Example
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value (i.e. 5).


class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # if the child value and root value is different start counting again
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result
