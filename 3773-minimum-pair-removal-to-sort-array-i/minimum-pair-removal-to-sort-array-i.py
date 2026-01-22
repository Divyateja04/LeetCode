class Solution(object):
    def minimumPairRemoval(self,nums):
        n = len(nums)
        operations = 0
        while True:
            is_sorted = True
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    is_sorted = False
                    break
            if is_sorted:
                break
            operations += 1
            min_sum = float('inf')
            min_index = -1
            for i in range(1, n):
                current_sum = nums[i - 1] + nums[i]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_index = i - 1
            nums[min_index] = min_sum
            for i in range(min_index + 1, n - 1):
                nums[i] = nums[i + 1]
            n -= 1
        return operations