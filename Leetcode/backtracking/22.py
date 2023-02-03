# 22. Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(left, right, path):
            # make sure '(' and ')' matches without this parentheses will not match
            if right < left:
                return
            if not left and not right:
                result.append(path)
                return
            if left:
                dfs(left - 1, right, path + '(')
            if right:
                dfs(left, right - 1, path + ')')

        dfs(n, n, '')
        return result