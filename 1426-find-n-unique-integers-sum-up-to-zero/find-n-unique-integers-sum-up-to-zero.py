class Solution(object):
    def sumZero(self, n):
        result = []
        for i in range(n // 2):
            result.append(i + 1)
            result.append((-1) * (i + 1))
        if n % 2 == 1:
            result.append(0)
        return result
        