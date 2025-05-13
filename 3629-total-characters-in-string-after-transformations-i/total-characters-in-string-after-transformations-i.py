class Solution(object):
    def lengthAfterTransformations(self, s, t):
        q = deque(itemgetter(*ascii_lowercase)(Counter(s)))
        for _ in range(t):
            q.appendleft(q.pop())
            q[1] += q[0]
        
        return sum(q)%(10**9+7)
        