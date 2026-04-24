class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = [False] * (n + 1)
        ans = set()
        cyclestart = 0
        def dfs(node, par):
            nonlocal cyclestart
            if visit[node]:
                cyclestart = node
                return True
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cyclestart > 0:
                        ans.add(node)
                    if node == cyclestart:
                        cyclestart = 0
                    return True
            return False

        dfs(1,-1)
        for u, v in reversed(edges):
            if u in ans and v in ans:
                return [u, v]
        return []