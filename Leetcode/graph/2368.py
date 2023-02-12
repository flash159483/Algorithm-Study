# 2368. Reachable Nodes With Restrictions
# Medium

# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
#
# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# You are also given an integer array restricted which represents restricted nodes.
#
# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.
#
# Note that node 0 will not be a restricted node.

# Example
# Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
# Output: 4
# Explanation: The diagram above shows the tree.
# We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        tree = collections.defaultdict(list)
        res = set(restricted)

        for a, b in edges:
            if a in res or b in res:
                continue
            tree[a].append(b)
            tree[b].append(a)

        self.result = 0

        def dfs(cur, prev):
            for i in tree[cur]:
                if i == prev:
                    continue
                dfs(i, cur)
            self.result += 1

        dfs(0, 0)
        return self.result
