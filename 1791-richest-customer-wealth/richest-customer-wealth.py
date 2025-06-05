class Solution(object):
    def maximumWealth(self, accounts):
        maxwealth = 0
        for i in range(len(accounts)):
            total_wealth = sum(accounts[i])
            maxwealth = max(maxwealth,total_wealth)
        return maxwealth
        