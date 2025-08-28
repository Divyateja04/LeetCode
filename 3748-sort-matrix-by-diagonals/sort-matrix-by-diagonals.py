class Solution(object):
    def sortMatrix(self, grid):
        n = len(grid)
        heap = []
        for m in range(n):
            for i in range(m + 1):
                heapq.heappush(heap, -grid[i + n - 1 - m][i])
            for j in range(m + 1):
                grid[j + n - 1 - m][j] = -heapq.heappop(heap)
        for m in range(n - 1):
            for i in range(m + 1):
                heapq.heappush(heap, grid[i][i + n - 1 - m])
            for j in range(m + 1):
                grid[j][j + n - 1 - m] = heapq.heappop(heap)
        return grid
        