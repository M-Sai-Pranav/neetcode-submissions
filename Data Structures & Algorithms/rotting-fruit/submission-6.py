from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        fresh_fruits = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh_fruits += 1 
                    
                
        visited = set()
        time_out = 0
        while queue:
            r,c,time = queue.popleft()
            time_out = time 
            positions = [ (r+1,c), (r-1,c), (r,c+1), (r,c-1) ]
            for pos in positions:
                r,c = pos 
                row_inbounds = 0 <= r < len(grid)
                col_inbounds = 0 <= c < len(grid[0])

                if not row_inbounds or not col_inbounds:
                    continue 
                
                if pos in visited:
                    continue 
                visited.add(pos)

                if grid[r][c] == 0:
                    continue 
                if grid[r][c] == 1:
                    queue.append((r,c,time+1))
                    fresh_fruits -= 1 
        if fresh_fruits > 0:
            return -1 
        if fresh_fruits == 0:
            return time_out              

