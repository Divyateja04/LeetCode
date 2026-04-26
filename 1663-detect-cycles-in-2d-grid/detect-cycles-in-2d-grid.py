class Solution(object):
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(x, y, px, py):
            visited[x][y] = True
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if grid[nx][ny] != grid[x][y]:
                    continue
                if not visited[nx][ny]:
                    if dfs(nx, ny, x, y):
                        return True
                elif nx != px or ny != py:
                    return True
            return False
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True
        return False