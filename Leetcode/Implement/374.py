# 374. Guess Number Higher or Lower
# Easy

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23


# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Example:
# Input: n = 10, pick = 6
# Output: 6

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while True:
            mid = (left + right) // 2
            check = guess(mid)
            if check == 0:
                return mid
            elif check == -1:
                right = mid - 1
            else:
                left = mid + 1