class Solution(object):
    def hasAlternatingBits(self, n):
        return(n^n//2)+1&n<1
        