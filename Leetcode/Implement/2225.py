# 2225. Find Players With Zero or One Losses
# Medium

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
#
# Return a list answer of size 2 where:
#
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
#
# Note:
#
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

# Example
# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, loses = [], []
        match = collections.defaultdict(int)

        for w, l in matches:
            match[w] = match[w] # defaultdict alway initialize with 0 if there is no lose matches match[w] == 0
            match[l] += 1

        for player, lose in match.items():
            if lose == 0:
                win.append(player)
            elif lose == 1:
                loses.append(player)

        return [sorted(win), sorted(loses)]