class Solution(object):
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word

        options=[]
        for i in range(len(word)):
            options.append(word[i:min(len(word),i+len(word)-numFriends+1)])

        options.sort(reverse=True)
        return options[0]