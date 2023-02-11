# 1129. Shortest Path with Alternating Colors
# Medium

# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1.
# Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
#
# You are given two arrays redEdges and blueEdges where:
#
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x
# such that the edge colors alternate along the path, or -1 if such a path does not exist.

# Example
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(lambda: collections.defaultdict(set))
        red, blue = 0, 1
        for a, b in redEdges:
            graph[a][red].add(b)

        for a, b in blueEdges:
            graph[a][blue].add(b)

        result = [sys.maxsize] * n
        visited = [[False] * 2 for _ in range(n)]
        visited[0][red] = True
        visited[0][blue] = True

        q = collections.deque([(0, red), (0, blue)])
        level = -1
        while q:
            level += 1
            for _ in range(len(q)):
                cur, color = q.popleft()
                result[cur] = min(result[cur], level)
                op_color = color ^ 1 # xor
                # check if there is a path with alternating color edge
                for i in graph[cur][op_color]:
                    if not visited[i][op_color]:
                        q.append((i, op_color))
                        visited[i][op_color] = True

        return [r if r != sys.maxsize else -1 for r in result]