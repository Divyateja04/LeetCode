class Solution(object):
    def maxAdjacentDistance(self, nums):
        max_diff = 0
        for i in range(len(nums)):
            next_index=(i+1) % len(nums)
            diff = abs(nums[i] - nums[next_index])
            max_diff = max(max_diff,diff)

        return max_diff
            
        