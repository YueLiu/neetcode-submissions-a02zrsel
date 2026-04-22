class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        q = deque()
        # visit.add(0)
        # q.append(0)
        ans = 0
        for node in range(n):
            if node not in visit:
                q.append(node)
                visit.add(node)
                while q:
                    curr = q.popleft()
                    for nei in adj[curr]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
                ans += 1
        return ans