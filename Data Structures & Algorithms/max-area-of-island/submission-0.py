class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count = max(count, self.dfs(grid, r, c, visited))
        return count 
    def dfs(self, grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])

        if not row_inbounds or not col_inbounds:
            return 0 
        
        if grid[r][c] == 0:
            return 0
        
        pos = (r,c)
        if pos in visited:
            return 0
        visited.add(pos)
        
        right = self.dfs(grid, r+1, c, visited)
        left = self.dfs(grid, r-1, c, visited)
        up = self.dfs(grid, r, c+1, visited)
        down = self.dfs(grid, r, c-1, visited)
        return 1 + right + left + up + down 

