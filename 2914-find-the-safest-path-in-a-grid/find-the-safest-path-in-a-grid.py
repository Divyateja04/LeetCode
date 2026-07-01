class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        safety_grid = [[-1] * n for _ in range(n)] 
        queue = [] 
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append([r, c])
                    safety_grid[r][c] = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            r, c = queue.pop(0) 
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < n and 0 <= new_c < n and safety_grid[new_r][new_c] == -1:
                    safety_grid[new_r][new_c] = safety_grid[r][c] + 1
                    queue.append([new_r, new_c])
        todo_list = [[safety_grid[0][0], 0, 0]] 
        safety_grid[0][0] = -1 
        while todo_list:
            todo_list.sort()
            safe_score, r, c = todo_list.pop()
            if r == n - 1 and c == n - 1:
                return safe_score
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < n and 0 <= new_c < n and safety_grid[new_r][new_c] != -1:
                    weakest_link = min(safe_score, safety_grid[new_r][new_c])
                    todo_list.append([weakest_link, new_r, new_c])
                    safety_grid[new_r][new_c] = -1                  
        return 0