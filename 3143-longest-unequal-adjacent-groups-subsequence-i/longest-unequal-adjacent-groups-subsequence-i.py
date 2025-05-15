class Solution(object):
    def getLongestSubsequence(self, words, groups):
        result = [words[0]]
        last_group = groups[0]

        for i in range(1, len(words)):
            if groups[i]  != last_group:
                result.append(words[i])
                last_group = groups[i]

        return result
        