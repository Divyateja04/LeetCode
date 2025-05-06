class Solution(object):
    def buildArray(self, nums):
        q=len(nums)
        for i in range(len(nums)):
            r=nums[i]
            b=nums[nums[i]]%q
            nums[i]=q*b+r
        for i in range(len(nums)):
            nums[i] =nums[i] //q
        return nums
        