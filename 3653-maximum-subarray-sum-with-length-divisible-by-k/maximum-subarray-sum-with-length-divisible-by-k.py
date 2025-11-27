class Solution(object):
    def maxSubarraySum(self, nums , k):
        n = len(nums)           
        a = [0] * n
        s = sum(nums[:k])   
        a[k-1] = s             
        r = s                  
        for i in range(k, n):
            s += nums[i] - nums[i-k]
            a[i] = s + (0 if 0 > a[i-k] else a[i-k])
            r = a[i] if a[i] > r else r
        
        return r