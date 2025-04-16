class Solution(object):
    def mergeAlternately(self, word1, word2):
        # Create a list to store the merged string
        answer = [''] * (len(word1) + len(word2))
        
        # Counters to keep track of remaining characters in word1 and word2
        firstCount = len(word1)
        secondCount = len(word2)

        # Pointers to track positions in the lists
        i = 0  # for answer list
        j = 0  # for word1 list
        k = 0  # for word2 list

        # Iterate until there are remaining characters in either word1 or word2
        while firstCount > 0 or secondCount > 0:
            # If there are remaining characters in word1, add the character to the answer list
            if firstCount > 0:
                answer[i] = word1[j]
                i += 1
                j += 1
                firstCount -= 1
            
            # If there are remaining characters in word2, add the character to the answer list
            if secondCount > 0:
                answer[i] = word2[k]
                i += 1
                k += 1
                secondCount -= 1

        # Create a new string from the answer list and return it as the result
        return ''.join(answer)