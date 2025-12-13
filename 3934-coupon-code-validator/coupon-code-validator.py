class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        validCoupons = []
        result = []
        allowed = {"electronics", "grocery", "pharmacy", "restaurant"}
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        def is_valid(coupon, active, line):
            if not active or not coupon or line not in allowed:
                return False
            for ch in coupon:
                if not (ch.isalnum() or ch == '_'):
                    return False
            return True
        for i in range(len(code)):
            if is_valid(code[i], isActive[i], businessLine[i]):
                validCoupons.append([code[i], businessLine[i]])
        for cat in order:
            temp = []
            for pair in validCoupons:
                if pair[1] == cat:
                    temp.append(pair[0])
            temp.sort()
            result.extend(temp)
        return result