class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                if self.explore(graph, i, visited) == True:
                    count+=1
        return count
    def explore(self, graph, node, visited):
        if node in visited:
            return False 
        visited.add(node)
        for n in graph[node]:
            self.explore(graph, n, visited) 
        return True 
    
