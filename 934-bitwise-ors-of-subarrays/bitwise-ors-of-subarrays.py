class Solution(object):
    def subarrayBitwiseORs(self, arr):
        ans=set(arr)
        one = set()
        one.add(arr[0])
        for i in  range(1,len(arr)):
            two=set()
            for j in one:
                two.add(j |  arr[i])
                ans.add(j| arr[i])
            two.add(arr[i])
            one = two
        return len(ans)
        