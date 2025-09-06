class Solution(object):
    def stepsum(self, n):
        if n <= 0:
            return 0
        res, base, step = 0, 1, 1
        while base <= n:
            cnt = min(n, base * 4 - 1) - base + 1
            res += cnt * step
            base *= 4
            step += 1
        return res

    def minOperations(self, queries):
        ans = 0
        for l, r in queries:
            total = self.stepsum(r) - self.stepsum(l - 1)
            ans += (total + 1) // 2
        return ans
        