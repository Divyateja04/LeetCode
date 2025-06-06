class Solution:
    def diagonalSum(self, A):
        n   = len(A)
        res = 0
        for i in range(n):
            res += A[i][i] + A[i][n-1-i]
        x = (n-1)//2
        return res - A[x][x] if n&1 else res