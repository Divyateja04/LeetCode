class Solution:
    def countSubmatrices(self, matrix, limit):
        rows = len(matrix)              
        cols = len(matrix[0])              
        sum_mat = [[0] * (cols + 1) for _ in range(rows + 1)] 
        result = 0                 
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                sum_mat[r][c] = matrix[r - 1][c - 1] \
                               + sum_mat[r - 1][c] \
                               + sum_mat[r][c - 1] \
                               - sum_mat[r - 1][c - 1]
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if sum_mat[r][c] <= limit:   
                    result += 1
        return result