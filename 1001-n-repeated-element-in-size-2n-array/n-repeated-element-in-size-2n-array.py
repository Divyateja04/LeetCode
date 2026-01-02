class Solution(object):
    def repeatedNTimes(self, nums):
        list1 = []
        for i in nums :
            if i in list1 :
                return i
            else :
                list1.append(i)
        