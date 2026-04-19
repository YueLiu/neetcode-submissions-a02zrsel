class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for c, p in prerequisites:
            indegree[p] += 1
            adj[c].append(p)
        
        q = deque()
        ans = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            c = q.popleft()
            ans.appendleft(c)
            for n in adj[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        if len(ans) == numCourses:
            return list(ans)
        else:
            return []
                

