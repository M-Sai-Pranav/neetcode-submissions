class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, r, c, visited) == True:
                    count+=1
        return count 
    def explore(self, grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            return False 
        if grid[r][c] == "0":
            return False 
        pos = (r, c)
        if pos in visited:
            return False 
        visited.add(pos)
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c-1, visited)
        self.explore(grid, r, c+1, visited)
        return True 