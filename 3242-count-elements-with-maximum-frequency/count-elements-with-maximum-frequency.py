class Solution(object):
    def maxFrequencyElements(self, nums):
        um = {}
        for x in nums:
            um[x] = um.get(x, 0) + 1
        maxi = 0
        for key, value in um.items():
            maxi = max(maxi, value)
        ans = 0
        for key, value in um.items():
            if value == maxi:
                ans += value
        return ans
        