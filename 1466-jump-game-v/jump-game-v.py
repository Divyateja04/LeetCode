class Solution(object):
    def maxJumps(self, arr, d):
        def dfs(i):
            if i in visited:
                return visited[i]
            a = []
            for r in range(i+1,min(i+d+1,len(arr))):
                if arr[r]>=arr[i]:
                    break
                if arr[i]>arr[r]:
                    a.append(dfs(r))  
            right = max(a) if a else 0
            b = []
            for l in range(i-1,max(-1,(i-d)-1),-1):
                if arr[i]<=arr[l]:break
                if arr[i]>arr[l]:
                    b.append(dfs(l))
            left = max(b) if b else 0
            visited[i] = 1 + max(left,right)
            return visited[i]
        visited = dict()
        res = 0
        for i in range(len(arr)):
            res = max(res,dfs(i))
        return res