class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[n] = 0
        from collections import defaultdict
        rules = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            rules[len(o)].append((o, c, w))
        import heapq
        trans_cost = {}
        for L, rule_list in rules.items():
            graph = defaultdict(list)
            nodes = set()
            for o, c, w in rule_list:
                graph[o].append((c, w))
                nodes.add(o)
                nodes.add(c)
            for start in nodes:
                pq = [(0, start)]
                dist = {start: 0}
                while pq:
                    cur_cost, u = heapq.heappop(pq)
                    if cur_cost > dist[u]:
                        continue
                    for v, w in graph[u]:
                        nc = cur_cost + w
                        if v not in dist or nc < dist[v]:
                            dist[v] = nc
                            heapq.heappush(pq, (nc, v))
                for end, cst in dist.items():
                    trans_cost[(L, start, end)] = cst
        for i in range(n - 1, -1, -1):
            # Case 1: no operation
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            for L in rules:
                if i + L > n:
                    continue
                s_sub = source[i:i + L]
                t_sub = target[i:i + L]
                if (L, s_sub, t_sub) in trans_cost:
                    dp[i] = min(
                        dp[i],
                        trans_cost[(L, s_sub, t_sub)] + dp[i + L]
                    )
        return dp[0] if dp[0] < INF else -1