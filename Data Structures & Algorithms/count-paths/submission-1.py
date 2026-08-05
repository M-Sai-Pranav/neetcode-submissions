class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def valid(r,c):
            if 0 <= r < m and 0 <= c < n:
                return True 
            return False 
        def path(r,c, path_count, m, n, memo):
            if r == m-1 and c == n-1:
                return 1 
            if (r,c) in memo:
                return memo[(r,c)]
            if valid(r,c):
                path_count = path(r, c+1, path_count, m, n, memo) + path(r+1, c, path_count, m, n, memo)
            memo[(r,c)] = path_count
            return path_count
        return path(0,0,0, m, n, {})

