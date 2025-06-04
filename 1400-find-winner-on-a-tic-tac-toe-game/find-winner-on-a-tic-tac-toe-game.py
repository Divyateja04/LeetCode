class Solution:
    def tictactoe(self, moves):
        scores = [0] * 8
        for i, (row, col) in enumerate(moves):
            if i % 2 == 0:  
                x = 1
            else:  
                x = -1
            scores[row] += x
            scores[col + 3] += x
            if row == col:
                scores[6] += x
            if 2 - row == col:
                scores[7] += x
        for score in scores:
            if score == 3:
                return 'A'
            elif score == -3:
                return 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'