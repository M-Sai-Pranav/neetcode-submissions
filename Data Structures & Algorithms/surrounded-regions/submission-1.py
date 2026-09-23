from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque([])
        for i in range(len(board[0])):
            if board[0][i] == "O":
                board[0][i] = "Y"
                queue.append((0,i))
        for i in range(len(board)):
            if board[i][0] == "O":
                board[i][0] = "Y"
                queue.append((i,0))
        rl = len(board)-1
        cl = len(board[0])-1 
        for i in range(len(board[0])):
            if board[rl][i] == "O":
                board[rl][i] = "Y"
                queue.append((rl, i))
        for i in range(len(board)):
            if board[i][cl] == "O":
                board[i][cl] = "Y"
                queue.append((i,cl))
        while queue:
            r,c = queue.popleft()
            positions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for pos in positions:
                r,c = pos
                row_inbounds = 0 <= r < len(board)
                col_inbounds = 0 <= c < len(board[0])

                if not row_inbounds or not col_inbounds:
                    continue 
                
                if board[r][c] == "O":
                    board[r][c] = "Y"
                    queue.append((r,c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "Y":
                    board[r][c] = "O"





