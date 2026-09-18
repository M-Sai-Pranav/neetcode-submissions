class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num_parents = {}
        for i in range(1, n+1):
            num_parents[i] = [0,0]

        for i,j in trust:
            num_parents[i][1] += 1 
            num_parents[j][0] += 1 
        
        for par, degree in num_parents.items():
            if degree[0] == n-1 and degree[1] == 0:
                return par 
        return -1 