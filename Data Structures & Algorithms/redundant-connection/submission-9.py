class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # topological sort
        n = len(edges)
        indegree = [0]*(n+1)
        adj = [[] for _ in range(n+1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        ans = set()
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)

        while q:
            curr = q.popleft()
            indegree[curr] -= 1
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for i in range(len(indegree)):
            if indegree[i] == 2:
                ans.add(i)
        
        for a, b in reversed(edges):
            if a in ans and b in ans:
                return [a, b]

