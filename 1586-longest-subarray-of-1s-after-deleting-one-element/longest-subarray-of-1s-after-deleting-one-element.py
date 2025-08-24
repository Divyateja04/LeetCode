class Solution(object):
    def longestSubarray(self, nums):
        i = 0
        j = 0
        n = len(nums)
        c0 = 0
        mx = 0
        while j < n:
            if nums[j] == 0:
                c0 += 1
            while i < n and c0 == 2:
                if nums[i] == 0:
                    c0 -= 1
                i += 1
            mx = max(j - i, mx)
            j += 1
        return mx
        