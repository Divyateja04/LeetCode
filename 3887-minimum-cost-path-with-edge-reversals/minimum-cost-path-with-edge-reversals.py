class Solution(object):
    def minCost(self, n, edges):
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,2*w))
        hq=[]
        dist=[float('inf')]*n
        dist[0]=0
        heapq.heappush(hq,(0,0))
        while hq:
            current_dist,curr_node=heapq.heappop(hq)
            if current_dist>dist[curr_node]:
                continue 
            for nextnode,w in adj[curr_node]:
                if dist[nextnode]>dist[curr_node]+w:
                    dist[nextnode]=dist[curr_node]+w
                    heapq.heappush(hq,(dist[nextnode],nextnode))
        return dist[n-1] if dist[n-1]!=float('inf') else -1