from collections import deque 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        surrounded_queue = deque([])
        for i in range(len(board[0])):
            if board[0][i] == "O":
                board[0][i] = "Y"
                surrounded_queue.append((0,i))
        for i in range(len(board)):
            if board[i][0] == "O":
                board[i][0] = "Y"
                surrounded_queue.append((i,0))
        last_row = len(board)-1
        last_col = len(board[0])-1
        for i in range(len(board[0])):
            if board[last_row][i] == "O":
                board[last_row][i] = "Y"
                surrounded_queue.append((last_row,i))
        for i in range(len(board)):
            if board[i][last_col] == "O":
                board[i][last_col] = "Y"
                surrounded_queue.append((i, last_col))
        visited = set()
        while surrounded_queue:
            r,c = surrounded_queue.popleft()
            positions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for pos in positions:
                r,c = pos 
                row_inbounds = 0 <= r < len(board)
                col_inbounds = 0 <= c < len(board[0])

                if not row_inbounds or not col_inbounds:
                    continue 

                if (r,c) in visited:
                    continue 
            
                if board[r][c] == "O":
                    surrounded_queue.append((r,c))
                    board[r][c] = "Y"
                    visited.add((r,c))
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "Y":
                    board[r][c] = "O"
        








