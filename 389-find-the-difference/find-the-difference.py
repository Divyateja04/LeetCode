class Solution(object):
    def findTheDifference(self, s, t):
        for i in set(t):
            if s.count(i) != t.count(i):
                return i

        