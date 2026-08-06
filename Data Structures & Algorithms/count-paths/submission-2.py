class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def valid(r,c,m,n):
            if 0 <= r < m and 0 <= c < n:
                return True 
            return False 
        def path(r,c,m,n,memo):
            if r == m-1 and c == n-1:
                return 1
            if not valid(r,c,m,n):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            left = path(r+1,c,m,n,memo)
            right = path(r,c+1,m,n,memo)
            memo[(r,c)] = left+right
            return left+right
        return path(0,0,m,n,{})