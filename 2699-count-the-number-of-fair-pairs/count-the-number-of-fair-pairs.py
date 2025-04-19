from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        cnt = 0
        n = len(nums)
        for i in range(n):
            left = lower - nums[i]
            right = upper - nums[i]
            l = bisect_left(nums, left, i + 1)
            r = bisect_right(nums, right, i + 1)
            cnt += r - l
        return cnt