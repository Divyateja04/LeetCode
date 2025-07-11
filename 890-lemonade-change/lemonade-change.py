class Solution:
    def lemonadeChange(self, bills):
        count5, count10 = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            elif bills[i] == 10:
                count10 += 1
                if not count5:
                    return False
                count5 -= 1
            else:
                if count10 and count5:
                    count10 -= 1
                    count5 -= 1
                elif count5 > 2:
                    count5 -= 3
                else:
                    return False
        return True