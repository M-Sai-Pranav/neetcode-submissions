from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque([])
        a_queue = deque([])

        p_result = []
        a_result = []

        for i in range(len(heights[0])):
            p_queue.append((0,i))
            p_result.append([0,i])

        for i in range(len(heights)):
            p_queue.append((i,0))
            p_result.append([i,0])
    
        bottom_row = len(heights)-1
        right_col = len(heights[0])-1
        for i in range(len(heights[0])):
            a_queue.append((bottom_row, i))
            a_result.append([bottom_row, i])

        for j in range(len(heights)):
            a_queue.append((j, right_col))
            a_result.append([j, right_col])
        

        p_visited = set()
        a_visited = set()

        while p_queue:
            r,c = p_queue.popleft()
            positions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for pos in positions:
                r1,c1 = pos
                row_inbounds = 0 <= r1 < len(heights)
                col_inbounds = 0 <= c1 < len(heights[0])
                

                if not row_inbounds or not col_inbounds:
                    continue 
                
                if pos in p_visited:
                    continue 

                if heights[r][c] <= heights[r1][c1]:
                    p_result.append([r1,c1])
                    p_queue.append((r1,c1))
                    p_visited.add(pos)

        while a_queue:
            r,c = a_queue.popleft()
            positions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for pos in positions:
                r1,c1 = pos
                row_inbounds = 0 <= r1 < len(heights)
                col_inbounds = 0 <= c1 < len(heights[0])
                

                if not row_inbounds or not col_inbounds:
                    continue 
                
                if pos in a_visited:
                    continue 

                if heights[r][c] <= heights[r1][c1]:
                    a_result.append([r1,c1])
                    a_queue.append((r1,c1))
                    a_visited.add(pos)

        common_set = set()
        for pos in p_result:
            r,c = pos[0], pos[1]
            common_set.add((r,c))
        final_res = []
        for pos in a_result:
            r,c = pos[0], pos[1]
            if (r,c) in common_set:
                final_res.append(pos)
        
        final_set = set()
        for pos in final_res:
            r,c = pos[0], pos[1]
            final_set.add((r,c))
        
        final_of_final = []
        for pos in final_set:
            r,c = pos 
            final_of_final.append([r,c])
    
        return final_of_final
         

