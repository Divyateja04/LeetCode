class Solution(object):
    def findKthNumber(self, n, k):
        def count_numbers_with_prefix(prefix, limit):
            count = 0
            current = prefix
            next_prefix = prefix + 1

            while current <= limit:
                count += min(next_prefix, limit + 1) - current
                current *= 10
                next_prefix *= 10
            return count
        current = 1
        k -= 1  

        while k > 0:
            children_count = count_numbers_with_prefix(current, n)
            if k >= children_count:
                k -= children_count
                current += 1
            else:
                current *= 10
                k -= 1

        return current