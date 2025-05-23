class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        base_sum = sum(nums)
        gains = [(num ^ k) - num for num in nums]
        gains.sort(reverse=True)
        max_gain=0
        current_gain=0
        count=0
        for gain in gains:
            current_gain += gain
            count += 1
            if count % 2 == 0:
                max_gain = max(max_gain,current_gain)
        return base_sum + max_gain
        