# 1578. Minimum Time to Make Rope Colorful
# Medium

# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
#
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help.
#     Bob can remove some balloons from the rope to make it colorful.
#     You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
#
# Return the minimum time Bob needs to make the rope colorful.
#

# Example:
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.

class Solution:
    def minCost(self, colors: str, time: List[int]) -> int:
        prev = result = 0
        for i in range(1, len(colors)):
            if colors[prev] != colors[i]:
                prev = i
            else:
                result += min(time[prev], time[i])
                if time[prev] < time[i]:
                    prev = i

        return result