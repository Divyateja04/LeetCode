class Solution(object):
    def numberOfSpecialChars(self, word):
        low = [False] * 26
        up = [False] * 26
        for c in word:
            if 'a' <= c <= 'z':
                low[ord(c) - ord('a')] = True
            else:
                up[ord(c) - ord('A')] = True
        ans = 0
        for i in range(26):
            if low[i] and up[i]:
                ans += 1
        return ans