class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_elements = set(nums)
        total_distinct_elements = len(set(nums))
        count=0
        n=len(nums)
        for i in range(n):
            current_set=set()
            for j in range(i,n):
                current_set.add(nums[j])
                if len(current_set) == total_distinct_elements:
                    count+=(n-j)
                    break
        return count 