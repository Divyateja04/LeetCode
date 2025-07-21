class Solution(object):
    def makeFancyString(self, s):
        stack=[]
        for letter in s:
            if len(stack) > 1 and letter == stack[-1] == stack[-2]:
                stack.pop()
            stack.append(letter)
        return ''.join(stack)
        