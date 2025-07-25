class Solution(object):
    def maxSum(self, nums):
        max_num = max(nums)
        if max_num <= 0:
            return max_num
        seen=0
        total = 0
        for x in nums:
            if x >=0and ((seen >> x) & 1) == 0:
                total +=x
                seen |= (1 << x) 

        return total       