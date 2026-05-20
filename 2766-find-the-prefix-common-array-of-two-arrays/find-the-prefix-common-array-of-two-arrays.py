class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        s1 = set()
        s2 = set()
        n = len(A)
        ans = [0] * n
        s1.add(A[0])  
        s2.add(B[0]) 
        if A[0] == B[0]:
            ans[0] = 1
        for i in range(1, n):
            temp = ans[i - 1]
            s1.add(A[i])  
            s2.add(B[i])
            if A[i] == B[i]:
                ans[i] = ans[i - 1] + 1  # Increment by exactly 1
            else:
                if A[i] in s2:
                    temp = temp + 1 
                if B[i] in s1:
                    temp = temp + 1  
                ans[i] = temp
        return ans