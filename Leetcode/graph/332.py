# 332. Reconstruct Itinerary
# Hard

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight.
# Reconstruct the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries,
# you should return the itinerary that has the smallest lexical order when read as a single string.
#
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

# Example
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # construct graph by lexical order, reason to reverse it is because in line 12 we have to access the first ticket
        # by pop(0) but this is O(n) time complexity by reversing it we can use pop() which is O(1)
        for ticket in sorted(tickets, reverse=True):
            graph[ticket[0]].append(ticket[1])

        result = []

        def dfs(cur):
            while graph[cur]:
                dfs(graph[cur].pop())
            result.append(cur)

        dfs("JFK")

        return result[::-1]
