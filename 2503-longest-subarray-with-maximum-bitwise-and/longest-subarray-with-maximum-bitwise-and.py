class Solution(object):
    def longestSubarray(self, nums):
        max_n=max(nums)
        return max(len(list(it)) for n, it in groupby(nums) if n== max_n)
        