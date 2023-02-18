# 227. Basic Calculator II
# Medium

# Given a string s which represents an expression, evaluate this expression and return its value.
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example
# Input: s = "3+2*2"
# Output: 7

class Solution:
    def calculate(self, s: str) -> int:
        def solve(sign, n):
            if sign == '+':
                stack.append(n)
            elif sign == '-':
                stack.append(-n)
            elif sign == '*':
                stack.append(stack.pop() * n)
            elif sign == '/':
                stack.append(int(stack.pop() / n))

        cur, stack, sign, num = 0, [], '+', 0

        while cur < len(s):
            if s[cur].isdigit():
                num = num * 10 + int(s[cur])

            elif s[cur] in '+-*/':
                solve(sign, num)
                num, sign = 0, s[cur]
            cur += 1

        solve(sign, num)
        return sum(stack)