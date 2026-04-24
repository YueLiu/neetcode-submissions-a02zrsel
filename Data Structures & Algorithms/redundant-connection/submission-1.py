class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        # DFS checks if there is ALREADY a path from 'source' to 'target'
        def dfs(node, target, visit):
            if node == target:
                return True
            
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    if dfs(nei, target, visit):
                        return True
            return False

        # Build forward, Left-to-Right
        for u, v in edges:
            visit = set()
            
            # If a path already exists between u and v, THIS is the redundant edge
            if dfs(u, v, visit):
                return [u, v]
                
            # Otherwise, it's safe to add the edge to the graph
            adj[u].append(v)
            adj[v].append(u)
            
        return []