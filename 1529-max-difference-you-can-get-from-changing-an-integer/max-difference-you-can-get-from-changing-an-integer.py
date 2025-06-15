class Solution(object):
    def maxDiff(self, num):
        s = list(str(num))
        for d in s:
            if d != '9':
                max_s = ''.join('9' if c == d else c for c in s)
                break
        else:
            max_s = ''.join(s)
        if s[0] != '1':
            d = s[0]
            min_s = ''.join('1' if c == d else c for c in s)
        else:
            for d in s[1:]:
                if d != '0' and d != '1':
                    min_s = ''.join('0' if c == d else c for c in s)
                    break
            else:
                min_s = ''.join(s)
        max_num = int(max_s)
        min_num = int(min_s)
        return max_num - min_num
        