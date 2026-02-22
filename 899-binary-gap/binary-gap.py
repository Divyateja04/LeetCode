class Solution(object):
    def binaryGap(self, n):
        binary = bin(n)[2:] 
        found_one = False
        is_one = 0
        ans = 0
        for i in range(len(binary)):
            if binary[i] == "1" and not found_one:
                is_one = i
                found_one = True
            elif binary[i] == "1" and found_one:
                ans = max(ans, i - is_one)
                is_one = i
        return ans