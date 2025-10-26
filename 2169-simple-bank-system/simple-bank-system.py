class Bank:
    def __init__(self, balance):
        self.dp = defaultdict(int)
        for i, amt in enumerate(balance):
            self.dp[i+1] = amt
        print(self.dp)
    def transfer(self, account1, account2, money) :
        if account1 in self.dp and account2 in self.dp: 
            bal = self.dp[account1]
            if bal >= money:
                self.dp[account1] -= money
                self.dp[account2] += money
                return True
            else:
                return False
        return False
    def deposit(self, account, money) :
        if account in self.dp:
            self.dp[account] += money
            return True
            
        return False
    def withdraw(self, account, money) :
        if account in self.dp:
            bal = self.dp[account]
            if bal >=money:
                self.dp[account] -= money
                return True
            else:
                return False
        else:    
            return False