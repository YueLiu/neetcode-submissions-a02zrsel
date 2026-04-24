class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        candidates = []
        root = -1

        def dfs(node,par):
            nonlocal root
            if node in visited:
                root = node
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei == root:
                    root = -1
                if dfs(nei,node):
                    candidates.append(nei)
                    return True
            return False


        dfs(1,-1)

        for a, b in reversed(edges):
            if a in candidates and b in candidates:
                return [a, b]

