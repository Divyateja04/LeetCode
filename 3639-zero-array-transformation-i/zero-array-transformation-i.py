class Solution(object):
    def isZeroArray(self, nums, queries):
        for i in range(len(nums)-1):
            nums[i]-=nums[i+1]
        for q in queries:
            if q[0]>0:
              nums[q[0]-1]+=1
            nums[q[1]]-=1
        for i in range(len(nums)-2, -1, -1):
            nums[i]+=nums[i+1]
        return all(a<=0 for a in nums)
        