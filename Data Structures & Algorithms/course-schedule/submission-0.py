class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
        for i,j in prerequisites:
            graph[i].append(j)
        visiting = set()
        visited = set()
        for i in range(numCourses):
            if self.cycle(graph, i, visiting, visited):
                return False
        return True
    def cycle(self, graph, node, visiting, visited):
        if node in visited:
            return False
        if node in visiting:
            return True 
        visiting.add(node)
        for n in graph[node]:
            if self.cycle(graph, n, visiting, visited):
                return True
        visiting.remove(node)
        visited.add(node)
        return False