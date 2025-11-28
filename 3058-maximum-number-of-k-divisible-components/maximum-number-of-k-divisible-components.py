class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        adj = [[] for _ in range(n + 1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        res = [0]  
        vis = [0] * n
        vis[0] = 1
        def dfs(node):
            leaf = values[node]
            vis[node] = 1
            for it in adj[node]:
                if vis[it] == 0:
                    leaf += dfs(it)
            if leaf % k == 0:
                res[0] += 1
                leaf = 0
            return leaf
        dfs(0)
        if res[0] == 0:
            return 1
        return res[0]