class Solution(object):
    def separateDigits(self, nums):
        count = 0
        for num in nums:
            temp = num
            while temp != 0:
                count += 1
                temp //= 10
        res = [0] * count
        idx = count - 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            while num != 0:
                res[idx] = num % 10
                idx -= 1
                num //= 10
        return res