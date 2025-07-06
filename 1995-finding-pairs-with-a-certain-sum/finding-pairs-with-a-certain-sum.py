class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        self.n1, self.n2 = Counter(nums1), Counter(nums2)
        self.n = [i for i in nums2]
        

    def add(self, index, val):
        self.n2[self.n[index]] -= 1
        self.n[index] += val
        self.n2[self.n[index]] += 1

    def count(self, tot):
        res = 0
        for j in self.n1:
            if tot - j in self.n2:
                res += self.n2[tot - j] * self.n1[j] 
        return res