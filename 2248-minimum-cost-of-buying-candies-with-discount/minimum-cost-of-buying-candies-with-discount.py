class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        ans = 0
        for i, val in enumerate(cost):
            if i % 3 != 2:
                ans += val
        return ans