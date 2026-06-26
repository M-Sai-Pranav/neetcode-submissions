from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, 0, 0, set()) > 0:
                    return self.explore(grid, 0, 0, set())
        return -1 
    def inbounds(self, grid, r, c):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        return row_inbounds and col_inbounds
    def explore(self, grid, r, c, visited):
        if grid[r][c] == 1:
            return -1 
        queue = deque([(r,c,1)])
        while queue:
            r,c,d = queue.popleft()
            if r == len(grid)-1 and c == len(grid[0])-1 and grid[r][c] == 0:
                return d
            directions = [ (-1,-1), (-1,0), (-1,1), 
                            (0,-1),          (0,1),
                            (1,-1), (1,0), (1,1)]
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if self.inbounds(grid, nr, nc) and (nr,nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr,nc))
                    queue.append((nr, nc, d+1))
        return -1
        