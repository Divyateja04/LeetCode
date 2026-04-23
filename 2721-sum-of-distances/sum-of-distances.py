from collections import defaultdict
class Solution:
    def distance(self, nums):
        n = len(nums)
        pos = defaultdict(list)
        for i in range(n):
            pos[nums[i]].append(i)
        res = [0] * n
        for el in pos:
            rem = sum(pos[el])
            left = 0
            leftctr = 0
            remctr = len(pos[el])
            for i in pos[el]:
                rem -= i
                remctr -= 1
                res[i] = i * leftctr - left + rem - remctr * i
                left += i
                leftctr += 1
        return res