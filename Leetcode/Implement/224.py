# 224. Basic Calculator
# Hard

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23


class Solution:
    def calculate(self, s: str) -> int:
        def solve(cur):
            def cal(sign, n):
                if sign == '+':
                    stack.append(n)
                elif sign == '-':
                    stack.append(-n)

            stack, sign, num = [], '+', 0

            while cur < len(s):
                if s[cur].isdigit():
                    num = num * 10 + int(s[cur])
                elif s[cur] in '+-':
                    cal(sign, num)
                    sign, num = s[cur], 0
                elif s[cur] == '(':
                    num, tmp = self.calculate(s[cur + 1:])
                    cur += tmp
                elif s[cur] == ')':
                    cal(sign, num)
                    return sum(stack), cur + 1
                cur += 1
            cal(sign, num)
            return sum(stack)

        return solve(0)