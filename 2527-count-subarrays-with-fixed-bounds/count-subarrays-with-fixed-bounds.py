class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        ans=0
        min_position=max_position=l=-1
        for i,num in enumerate(nums):
            if num <minK or num >maxK:
                l=i
            if num == minK:
                min_position = i
            if num == maxK:
                max_position = i
            ans+=max(0,min(min_position,max_position) -l)
        return ans
        