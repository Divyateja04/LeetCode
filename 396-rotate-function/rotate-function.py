class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        ans = F
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            ans = max(ans, F)
        return ans