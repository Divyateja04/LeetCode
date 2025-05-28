class Solution(object):
    def isMonotonic(self, nums):
        if nums == sorted(nums) or nums == sorted(nums,reverse=True):
            return True
        return False
        