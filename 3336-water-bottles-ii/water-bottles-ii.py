class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        total = numBottles   
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            numBottles = 1   
            total += 1
            empty += numBottles   
            numExchange += 1      
        
        return total
        