class Solution(object):
    def countOdds(self, low, high):
        c=high-low+1
        if low%2!=0 and high%2!=0:
            b=c//2+1
        else:
            b=c//2
        return(b)