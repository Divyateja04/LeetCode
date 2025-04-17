class Solution:
    def countPairs(self, nums, k):
        index = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        index += 1
        return index