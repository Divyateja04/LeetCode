class Solution(object):
    def avoidFlood(self, A):
        nxt = list(range(len(A) + 1))
        pre = {}
        res = [1] * len(A)
        def find(i):
            j=i if nxt[i] == i else find(nxt[i])
            nxt[i] = j + 1
            return j

        for i,a in enumerate(A):
            if a == 0: continue
            nxt[i] = i + 1
            if a in pre:
                j = find(pre[a])
                if j > i:
                    return []
                res[j] = a
            res[i] = -1
            pre[a] = i
        return res
        