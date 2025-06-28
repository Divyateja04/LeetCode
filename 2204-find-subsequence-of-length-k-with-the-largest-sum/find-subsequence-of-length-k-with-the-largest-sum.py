class Solution:
    def maxSubsequence(self, a, k):
        return [v for _,v in sorted(nlargest(k,enumerate(a),itemgetter(1)))]