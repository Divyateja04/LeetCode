class Solution(object):
    def minPairSum(self, numbers):
        numbers.sort()
        start, end = 0, len(numbers) - 1
        max_pair = 0
        while start < end:
            pair_sum = numbers[start] + numbers[end]
            max_pair = max(max_pair, pair_sum)
            start += 1
            end -= 1
        return max_pair