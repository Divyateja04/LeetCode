class Solution(object):
    def pairSum(self, head):
        twin_sum = 0
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        for i in range(n//2):
            twin_sum = max(twin_sum, arr[i] + arr[n-i-1])
        return twin_sum