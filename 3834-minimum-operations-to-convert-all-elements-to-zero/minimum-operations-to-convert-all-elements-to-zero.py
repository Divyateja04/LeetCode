class Solution(object):
    def minOperations(self, nums):
        st = []
        ans = 0
        for num in nums:
            while len(st) > 0 and num < st[-1]:
                st.pop()
            if len(st) == 0 or num > st[-1]:
                if num == 0:
                    continue
                ans += 1
                st.append(num)
        return ans