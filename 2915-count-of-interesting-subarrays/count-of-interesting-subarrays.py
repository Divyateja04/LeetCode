class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        has = {}
        p=c=0
        for i in range(len(nums)):
            has[p%modulo] = has.get(p%modulo,0) +1
            if nums[i]%modulo == k:
                p+=1
            c+=has.get((p%modulo-k)%modulo,0)
        return c

        