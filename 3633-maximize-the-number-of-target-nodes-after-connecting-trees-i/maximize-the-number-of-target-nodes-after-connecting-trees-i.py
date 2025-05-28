class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        def build_graph(edges):
            graph = [[] for _ in range(len(edges) + 1)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def dfs(graph, node, parent, steps):
            if steps == 0:
                return 1
            count = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    count += dfs(graph, neighbor, node, steps - 1)
            return 1 + count

        graph1 = build_graph(edges1)
        graph2 = build_graph(edges2)

        max_reachable_in_graph2 = 0
        if k > 0:
            for i in range(len(graph2)):
                max_reachable_in_graph2 = max(max_reachable_in_graph2, dfs(graph2, i, -1, k - 1))

        result = []
        for i in range(len(graph1)):
            reachable_in_graph1 = dfs(graph1, i, -1, k)
            result.append(max_reachable_in_graph2 + reachable_in_graph1)

        return result