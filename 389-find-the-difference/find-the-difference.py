class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in set(t):
            if s.count(i) != t.count(i) :
                return i

        