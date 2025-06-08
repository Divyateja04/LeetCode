class Solution(object):
    def lexicalOrder(self, n):
        res = [1]
        
        while len(res) < n:
            last = res[-1]

            if last * 10 <= n:
                res.append(last * 10)
            elif last + 1 <= n and (last + 1) % 10 != 0:
                res.append(last + 1)
            else:
                last = last + 1 if (last + 1) % 10 == 0 else last // 10 + 1
                
                while last % 10 == 0:
                    last //= 10
                res.append(last)

        return res