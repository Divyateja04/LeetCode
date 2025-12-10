class Solution(object):
    def __init__(self):
        self.mod = 1000000007

    def count(self, arr, a):
        if a == len(arr):
            return 1

        if arr[a] <= arr[0]:
            return 0

        return (a * self.count(arr, a + 1)) % self.mod

    def countPermutations(self, complexity):
        return self.count(complexity, 1)