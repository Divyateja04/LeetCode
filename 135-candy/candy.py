class Solution(object):
    def candy(self, ratings):
        res=len(ratings) * [1]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1]+1
        for i in xrange(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1],res[i]+1)
        return sum(res) 
        