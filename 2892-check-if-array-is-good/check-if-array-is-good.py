class Solution(object):
    def isGood(self, nums):
        n = len(nums) - 1
        n_count = 0
        visited = 0 
        for num in nums:
            if num > n:
                return False
            elif num == n:
                n_count += 1
                if n_count > 2:
                    return False
            else:
                if visited & (1 << num):
                    return False
                visited |= (1 << num)
        if n_count < 2:
            return False
        return visited == (1 << n) - 2