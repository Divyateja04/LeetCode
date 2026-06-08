class Solution(object):
    def pivotArray(self, nums, pivot):
        less = []
        equals = [] 
        greater = []

        for num in nums:
            if pivot > num:
                less.append(num)
            elif pivot < num:
                greater.append(num)
            else:
                equals.append(num)
        less.extend(equals)
        less.extend(greater) 
        return less