class Solution(object):
    def minDeletionSize(self, strs):
        n = len(strs[0]) 
        def checkRest(idx1, idx2):
            for i in range(1, len(strs)):
                if not strs[i][idx1] <= strs[i][idx2]: 
                    return False
            return True       
        def lis(idx, memo):
            if idx in memo:
                return memo[idx]  
            longest = 1
            for i in range(idx + 1, n):
                if strs[0][idx] <= strs[0][i] and checkRest(idx, i):
                    longest = max(longest, 1 + lis(i, memo))            
            memo[idx] = longest
            return longest
        longest = 0
        memo = {}
        for i in range(n):
            longest = max(longest, lis(i, memo))
        return n - longest