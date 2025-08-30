class Solution(object):
    def isValidSudoku(self, board):
        return 1 == max(collections.Counter(
            x
            for i,row in enumerate(board)
            for j,c in enumerate(row)
            if c !='.'
            for x in ((c,i) , (j,c), (i/3, j/3, c))
        ).values() + [1])
        