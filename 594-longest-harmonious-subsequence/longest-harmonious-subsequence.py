class Solution(object):
    def findLHS(self, nums):
        tmp= Counter(nums)
        keys=tmp.keys()
        max=0
        for num in keys:
            if num -1 in keys:
                if tmp[num-1]+ tmp[num] > max:
                    max = tmp[num-1]+tmp[num]
        return max
        