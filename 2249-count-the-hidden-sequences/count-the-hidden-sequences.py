class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        count = 0
        n = len(differences)

        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + differences[i]

        
        min_offset = min(prefix)
        max_offset = max(prefix)

        
        for start in range(lower, upper + 1):
            min_val = start + min_offset
            max_val = start + max_offset
            if min_val >= lower and max_val <= upper:
                count += 1

        return count