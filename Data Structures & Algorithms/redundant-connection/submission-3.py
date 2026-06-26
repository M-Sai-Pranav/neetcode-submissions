class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i,j in edges:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            visited = set()
            res = self.explore(graph, i, j, visited)
            if res == True:
                return [i,j]
            graph[i].append(j)
            graph[j].append(i)
        return []
        
    def explore(self, graph, curr, target, visited):
        if curr == target:
            return True
        visited.add(curr)
        for n in graph[curr]:
            if n not in visited:
                if self.explore(graph, n, target, visited):
                    return True 
        return False