class Solution(object):
    def findWordsContaining(self, words, x):
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result
        