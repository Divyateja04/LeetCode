class Solution(object):
    def minDeletionSize(self, strs):
        ret = 0
        for c in zip(*strs): 
            if list(c) != sorted(c): 
                ret += 1       
        return ret 
        