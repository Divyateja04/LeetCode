class Solution(object):
    def constructTransformedArray(self, nums):
        return [nums[(i + num % len(nums) + len(nums)) % len(nums)] for i, num in enumerate(nums)]
        