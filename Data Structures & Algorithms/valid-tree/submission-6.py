class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no loop and all connected

        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q = deque()
        q.append([0,-1])
        visited = set()
        visited.add(0)
        # visited
        while q:
            c, p = q.popleft()
            for nei in adj[c]:
                if nei != p and nei not in visited:
                    q.append([nei,c])
                    visited.add(nei)
        return len(visited) == n
                



        

        