class Solution(object):
    def minimumCost(self, nums, k, dist):
        L = len(nums)
        M = k - 1
        from sortedcontainers import SortedList
        topk = SortedList()
        rest = SortedList()
        idx = 1
        step = 0
        while step <= dist:
            topk.add(nums[idx + step])
            if len(topk) > M:
                rest.add(topk.pop())
            step += 1
        mini = sum(topk)
        temp = mini
        while idx + dist < L - 1:
            left = nums[idx]
            idx_left = topk.bisect_left(left)
            if idx_left == M or topk[idx_left] != left:
                rest.remove(left)
            else:
                topk.remove(left)
                temp -= left
            idx += 1
            right = nums[idx + dist]
            rest.add(right)
            if len(topk) < M:
                to_add = rest[0]
                topk.add(rest.pop(0))
                temp += to_add
            else:
                if rest[0] < topk[-1]:
                    to_add = rest[0]
                    to_remove = topk[-1]
                    topk.pop()
                    topk.add(to_add)
                    rest.pop(0)
                    rest.add(to_remove)
                    temp += to_add
                    temp -= to_remove
            mini = min(mini, temp)
        ans = nums[0] + mini
        return ans