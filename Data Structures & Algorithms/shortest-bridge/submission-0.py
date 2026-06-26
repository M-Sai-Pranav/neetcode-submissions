from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        main_bridge = None 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                potential_bridge = self.explore(grid, r, c, set())
                if len(potential_bridge) > 0:
                    main_bridge = potential_bridge
                    break 
        visited = set(main_bridge)
        queue = deque([])
        for r,c in main_bridge:
            queue.append((r,c,0))
        while queue:
            r,c,d = queue.popleft()
            if grid[r][c] == 1 and (r,c) not in main_bridge:
                return d-1 
            if self.inbounds(grid, r-1, c) and (r-1,c) not in visited:
                visited.add((r-1,c))
                queue.append((r-1,c,d+1))
            if self.inbounds(grid, r+1, c) and (r+1,c) not in visited:
                visited.add((r+1,c))
                queue.append((r+1,c,d+1))
            if self.inbounds(grid, r, c-1) and (r,c-1) not in visited:
                visited.add((r,c-1))
                queue.append((r,c-1,d+1))
            if self.inbounds(grid, r, c+1) and (r,c+1) not in visited:
                visited.add((r,c+1))
                queue.append((r,c+1,d+1))

        
    def inbounds(self, grid, r, c):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        return row_inbounds and col_inbounds 
    def explore(self,grid, r, c, visited):
        if not self.inbounds(grid, r, c) or grid[r][c] == 0:
            return visited
        pos = (r,c)
        if pos in visited:
            return visited
        visited.add(pos)
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c-1, visited)
        self.explore(grid, r, c+1, visited)
        return visited










