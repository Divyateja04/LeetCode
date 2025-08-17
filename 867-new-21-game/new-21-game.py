class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k==0 or n>=k+maxPts:
            return 1.0
        dp=[1.0]+[0.0]*n
        s=1.0
        r=0.0
        m=1.0/maxPts
        for i in range(1,n+1):
            dp[i]=s*m
            if i<k:
                s+=dp[i]
            else:
                r+=dp[i]
            if i>=maxPts:
                s-=dp[i-maxPts]
        return r
        