"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            clone = Node(node.val, [])
            visited[node] = clone
            for v in node.neighbors:
                clone.neighbors.append(dfs(v))
            return clone
        
        return dfs(node) if node else None
