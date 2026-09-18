"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {})
    def dfs(self, node, visited_dict):
        if node is None:
            return 
        if node in visited_dict:
            return visited_dict[node]
        visited_dict[node] = Node(node.val, [])
        for nei in node.neighbors:
            copy_nei = self.dfs(nei, visited_dict)
            visited_dict[node].neighbors.append(copy_nei)
        return visited_dict[node]