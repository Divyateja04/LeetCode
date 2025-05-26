class Solution(object):
    def largestPathValue(self, colors, edges):
        from collections import defaultdict

        n = len(colors)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        count = [[0]*26 for _ in range(n)]
        vis = [0]*n

        def dfs(node):
            if vis[node] == 1:
                return float('inf')  # cycle
            if vis[node] == 2:
                return max(count[node])
            vis[node] = 1
            for nei in adj[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')
                for i in range(26):
                    count[node][i] = max(count[node][i], count[nei][i])
            count[node][ord(colors[node]) - ord('a')] += 1
            vis[node] = 2
            return max(count[node])

        ans = 0
        for i in range(n):
            res = dfs(i)
            if res == float('inf'):
                return -1
            ans = max(ans, res)
        return ans