class Solution(object):
    def isPowerOfFour(self, n):
        return (n & (n-1)) == 0 and n % 3 == 1
        