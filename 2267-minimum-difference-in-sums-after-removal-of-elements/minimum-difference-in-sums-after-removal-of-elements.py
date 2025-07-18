class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums) // 3
        left_part = []
        left_sum = 0
        prefix = [0] * (2 * n)

        for i in range(0, 2 * n):
            heapq.heappush(left_part, -nums[i])
            left_sum += nums[i]

            if len(left_part) > n :
                pop_large_element = heapq.heappop(left_part)
                left_sum -= -pop_large_element

            if i >= n - 1:
                prefix[i] = left_sum
        right_part = []
        right_sum = 0
        suffix = [0] * (2 * n)

        for i in reversed(range(n, 3 * n)):
            heapq.heappush(right_part, nums[i])
            right_sum += nums[i]

            if len(right_part) > n:
                pop_small_element = heapq.heappop(right_part)
                right_sum -= pop_small_element

            if i <= 2 * n:
                suffix[i - n] = right_sum
        minimum = float('inf')  
        for i in range(n - 1, 2 * n):
            diff = prefix[i] - suffix[i + 1 - n]
            minimum = min(minimum, diff)

        return minimum