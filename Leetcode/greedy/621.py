# 621. Task Scheduler
# Medium

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
# Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array),
# that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Example
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            c = 0
            for t, _ in counter.most_common(n + 1):
                c += 1
                result += 1

                counter.subtract(t)
                # remove item smaller or equal to 0
                counter += collections.Counter()

            if not counter:
                break
            result += n - c + 1

        return result