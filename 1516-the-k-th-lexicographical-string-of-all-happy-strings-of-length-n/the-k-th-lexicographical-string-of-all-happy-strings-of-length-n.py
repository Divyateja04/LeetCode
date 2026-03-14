class Solution(object):
    def getHappyString(self, n, k):
        if k > (3 << (n - 1)):  
            return ""  
        queue = deque([""])  
        while k:
            curr = queue.popleft()
            for c in "abc":
                if not curr or curr[-1] != c:
                    queue.append(curr + c)
                    if len(curr) + 1 == n:
                        k -= 1
                if k == 0:
                    break
        return queue[-1]