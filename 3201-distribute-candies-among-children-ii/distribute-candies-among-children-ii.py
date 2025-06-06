class Solution(object):
    def distributeCandies(self, n, limit):
        res = 0
        for f in range(min(n, limit) + 1):
            rem = n - f
            a = max(rem - limit, 0)
            b = min(rem, limit)
            if a <= b:
                res += b - a + 1
        return res
        