# 1626. Best Team With No Conflicts
# Medium

# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score.
# The score of the team is the sum of scores of all the players in the team.
#
# However, the basketball team is not allowed to have conflicts.
# A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.
#
# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively,
# return the highest overall score of all possible basketball teams.

#Example
# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # sort the score according to age
        score_age = sorted([age, score] for age, score in zip(ages, scores))

        dp = [0] * 1001
        for i in range(len(scores)):
            dp[i] = score_age[i][1]
            for j in range(i):
                # age does not matter since it is sorted score is the key here
                if score_age[i][1] >= score_age[j][1]:
                    dp[i] = max(dp[i], dp[j] + score_age[i][1])

        return max(dp)