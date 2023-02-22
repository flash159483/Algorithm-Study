# 1011. Capacity To Ship Packages Within D Days
# Medium

# A conveyor belt has packages that must be shipped from one port to another within days days.
#
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# example
# Input                 Output
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
#
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid, need, total = (l + r) // 2, 1, 0

            for w in weights:
                if w + total > mid:
                    need += 1
                    total = 0
                total += w

            if need > days:
                l = mid + 1
            else:
                r = mid

        return l