class Solution(object):
    def maxDistance(self, nums1, nums2):
        i,j = 0,0
        n,m = len(nums1), len(nums2)
        ans = 0
        while i < n and j < m :
            if j < i :
                j = i
            if j >= m:
                break
            if nums1[i] <= nums2[j]:
                ans = max(ans, j-i)
                j += 1
            else:
                i += 1
        return ans