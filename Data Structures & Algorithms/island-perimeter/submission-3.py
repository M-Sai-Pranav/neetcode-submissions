class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return self.dfs(grid, r, c, set())
                    
        
    def dfs(self, grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            return 1 
        if row_inbounds and col_inbounds and grid[r][c] == 0:
            return 1
        if row_inbounds and col_inbounds and (r,c) in visited:
            return 0
        if row_inbounds and col_inbounds and grid[r][c] == 1:
            visited.add((r,c))
            
        a = self.dfs(grid, r+1, c, visited)
        b = self.dfs(grid, r-1, c, visited)
        k = self.dfs(grid, r, c+1, visited)
        d = self.dfs(grid, r, c-1, visited)

        return a + b + k + d 
