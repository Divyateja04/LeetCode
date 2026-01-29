class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        ALPHABET_SIZE = 26
        import math
        inf = float('inf')
        dist = [[inf] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
        for i in range(ALPHABET_SIZE):
            dist[i][i] = 0       
        for i in range(len(original)):
            o_idx = ord(original[i]) - ord('a')
            c_idx = ord(changed[i]) - ord('a')
            dist[o_idx][c_idx] = min(dist[o_idx][c_idx], cost[i])        
        for k in range(ALPHABET_SIZE):
            for i in range(ALPHABET_SIZE):
                for j in range(ALPHABET_SIZE):
                    if dist[i][k] < inf and dist[k][j] < inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])     
        total_cost = 0
        n = len(source)
        for i in range(n):
            src_idx = ord(source[i]) - ord('a')
            tgt_idx = ord(target[i]) - ord('a')
            min_cost = dist[src_idx][tgt_idx]            
            if min_cost == inf:
                return -1             
            total_cost += min_cost        
        return total_cost