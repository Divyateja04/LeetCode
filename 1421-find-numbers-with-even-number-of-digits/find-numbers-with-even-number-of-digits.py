class Solution(object):
    def findNumbers(self, nums):
        count=0
        for num in nums:
            if int(math.log10(num) + 1) % 2 == 0:
                count += 1
        return count