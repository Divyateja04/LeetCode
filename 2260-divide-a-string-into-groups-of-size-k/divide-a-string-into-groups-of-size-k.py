class Solution(object):
    def divideString(self, s, k, fill):
        n = len(s)
        groups = (n + k - 1) // k
        result = []

        for i in range(groups):
            group = ''
            for j in range(k):
                index = i * k + j
                if index < n:
                    group += s[index]
                else:
                    group += fill  # Padding
            result.append(group)

        return result
        