class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        h_dist = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_dist.add(abs(hFences[i] - hFences[j]))
        ans = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                d = abs(vFences[i] - vFences[j])
                if d in h_dist:
                    ans = max(ans, d * d)
        return ans % MOD if ans != -1 else -1