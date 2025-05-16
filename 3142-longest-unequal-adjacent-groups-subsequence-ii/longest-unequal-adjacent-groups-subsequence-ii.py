class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        def eq(x, y):
            if len(x) != len(y): return False
            return sum(ch1 != ch2 for ch1, ch2 in zip(x, y)) == 1
        
        size = len(words)
        dp = [(1, -1)] * size
        for i in range(1, size):
            for j in range(i):
                if groups[i] != groups[j] and eq(words[i], words[j]):
                    tmp = (dp[j][0] + 1, j)
                    dp[i] = max(dp[i], tmp, key=lambda x: x[0])
        cur = max(range(size), key=lambda x: dp[x][0])
        ans = []
        while cur != -1:
            ans.append(words[cur])
            cur = dp[cur][1]
        return ans[::-1]
        