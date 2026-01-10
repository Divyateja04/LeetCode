class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[-1] * m for _ in range(n)]

        def solve(i, j):
            if i >= n and j >= m:
                return 0

            if i >= n:
                return sum(ord(s2[k]) for k in range(j, m))

            if j >= m:
                return sum(ord(s1[k]) for k in range(i, n))

            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = solve(i + 1, j + 1)
            else:
                delete_s1 = ord(s1[i]) + solve(i + 1, j)
                delete_s2 = ord(s2[j]) + solve(i, j + 1)
                dp[i][j] = min(delete_s1, delete_s2)

            return dp[i][j]

        return solve(0, 0)