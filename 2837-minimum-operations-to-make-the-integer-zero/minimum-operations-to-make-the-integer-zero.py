class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        for i in range(1,61):
            r=num1-(i*num2) 
            if r<=0: 
                break
            m=bin(r).count('1') 
            if m<=i<=r: 
                return i 
        return -1
        