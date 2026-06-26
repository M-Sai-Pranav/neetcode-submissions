from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ans = 0
        if self.explore(grid, 0, 0, set(), ans) > 0:
            return self.explore(grid, 0, 0, set(), ans)
        return -1 
    def inbounds(self, grid, r, c):
        row = 0 <= r < len(grid)
        col = 0 <= c < len(grid[0])
        return row and col
    def explore(self, grid, r, c, visited, ans):
        if grid[r][c] == 1:
            return -1
        visited.add((r,c))
        queue = deque([(r,c,1)])

        while queue:
            r,c,d = queue.popleft()
            if r == len(grid)-1  and c == len(grid[0])-1 and grid[r][c] == 0:
                return d
            if grid[r][c] == 1:
                continue
            if self.inbounds(grid, r-1, c-1) and (r-1,c-1) not in visited and grid[r-1][c-1] == 0:
                visited.add((r-1,c-1))
                queue.append((r-1,c-1,d+1))
            if self.inbounds(grid, r-1, c) and (r-1,c) not in visited and grid[r-1][c] == 0:
                visited.add((r-1,c))
                queue.append((r-1,c,d+1))
            if self.inbounds(grid, r-1, c+1) and (r-1,c+1) not in visited and grid[r-1][c+1] == 0:
                visited.add((r-1,c+1))
                queue.append((r-1,c+1,d+1))
            if self.inbounds(grid, r, c-1) and (r,c-1) not in visited and grid[r][c-1] == 0:
                visited.add((r,c-1))
                queue.append((r,c-1,d+1))
            if self.inbounds(grid, r, c+1) and (r,c+1) not in visited and grid[r][c+1] == 0:
                visited.add((r,c+1))
                queue.append((r,c+1,d+1))
            if self.inbounds(grid, r+1, c-1) and (r+1,c-1) not in visited and grid[r+1][c-1] == 0:
                visited.add((r+1,c-1))
                queue.append((r+1,c-1,d+1))
            if self.inbounds(grid, r+1, c+1) and (r+1,c+1) not in visited and grid[r+1][c+1] == 0:
                visited.add((r+1,c+1))
                queue.append((r+1,c+1,d+1))
            if self.inbounds(grid, r+1, c,) and (r+1,c) not in visited and grid[r+1][c] == 0:
                visited.add((r+1,c))
                queue.append((r+1,c,d+1))
        return -1
