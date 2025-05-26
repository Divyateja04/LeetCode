class Solution(object):
    def arraySign(self, nums):
        res=1
        for x in nums:
            if x>0:
                res*=1
            elif x<0:
                res*=-1
            else:
                return 0
        return res
        