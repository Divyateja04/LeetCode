class Solution(object):
    def countTriples(self, n):
        count = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                s = a*a + b*b
                c = int(s**0.5)
                if c <= n and c*c == s:
                    count += 1
        return count * 2