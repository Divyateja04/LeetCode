class Solution(object):
    def countOdds(self, low, high):
        if low % 2 == 1:
            low = low - 1
        if high % 2 == 1:
            high = high + 1       
        return (high-low)/2