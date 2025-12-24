class Solution(object):
    def minimumBoxes(self, apple, capacity):
        sum_val = sum(apple)
        capacity.sort()
        count = 0
        j = len(capacity) - 1
        while sum_val > 0:
            sum_val -= capacity[j]
            count += 1
            j -= 1
        return count