# 2306
# Hard

# You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:
#
# Choose 2 distinct names from ideas, call them ideaA and ideaB.
# Swap the first letters of ideaA and ideaB with each other.
# If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
# Otherwise, it is not a valid name.
# Return the number of distinct valid names for the company.

# Example
# Input: ideas = ["coffee","donuts","time","toffee"]
# Output: 6
# Explanation: The following selections are valid:
# - ("coffee", "donuts"): The company name created is "doffee conuts".
# - ("donuts", "coffee"): The company name created is "conuts doffee".
# - ("donuts", "time"): The company name created is "tonuts dime".
# - ("donuts", "toffee"): The company name created is "tonuts doffee".
# - ("time", "donuts"): The company name created is "dime tonuts".
# - ("toffee", "donuts"): The company name created is "doffee tonuts".
# Therefore, there are a total of 6 distinct company names.
#
# The following are some examples of invalid selections:
# - ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
# - ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
# - ("coffee", "toffee"): Both names formed after swapping already exist in the original array.


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        table = collections.defaultdict(set)

        for i in ideas:
            table[i[0]].add(i[1:])

        result = 0
        for i, a in table.items():
            for j, b in table.items():
                if i >= j:
                    continue

                re = len(a & b)
                result += (len(a) - re) * (len(b) - re)

        return result * 2