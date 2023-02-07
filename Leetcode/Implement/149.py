# 149. Max Points on a Line
# Hard

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.


# Example
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        result = 1
        for i, p1 in enumerate(points):
            table = collections.defaultdict(int)
            for p2 in points[i+1:]:
                x1, y1 = p1
                x2, y2 = p2
                if x1 - x2 == 0:
                    s = sys.maxsize
                    table[s] += 1
                else:
                    s = (y1-y2) / (x1-x2)
                    table[s] += 1
                result = max(table[s], result)
        return result+1
