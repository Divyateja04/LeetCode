class Solution(object):
    def countHillValley(self, nums):
        hillValley = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:    
                hillValley += 1
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:    
                hillValley += 1
        return hillValley
        