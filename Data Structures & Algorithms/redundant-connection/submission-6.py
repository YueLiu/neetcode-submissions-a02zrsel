class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        def dfs(node,par):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True
            return False

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited = set()
            if dfs(a,-1):
                return [a,b]