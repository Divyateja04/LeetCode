class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        mod = 10**9 + 7
        dp = [[[0, 0] for j in range(zero+1)] for i in range(one+1)]
        for j in range(min(zero, limit) + 1):
            dp[0][j][0] = 1
        for i in range(min(one, limit) + 1):
            dp[i][0][1] = 1
        dp[0][0] = [0, 0]
        for i in range(1, one+1):
            for j in range(1, zero+1):
                dp[i][j][0] = dp[i][j-1][1] + dp[i][j-1][0]
                if j >= limit + 1:
                    dp[i][j][0] -= dp[i][j-limit-1][1]
                dp[i][j][0] %= mod
                dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j][1]
                if i >= limit + 1:
                    dp[i][j][1] -= dp[i-limit-1][j][0]
                dp[i][j][1] %= mod
        return sum(dp[one][zero]) % mod