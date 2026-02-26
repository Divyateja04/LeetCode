class Solution(object):
    def numSteps(self, s):
        result ,v = 0, int(s,2)
        while v > 1:
            if v%2:
                v+= 1
            else:
                v >>= 1
            result += 1
        return result