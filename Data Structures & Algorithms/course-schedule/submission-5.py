class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for c, p in prerequisites:
            indegree[p] += 1
            adj[c].append(p)
        
        q = deque()

        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        remove = 0
        while q:
            currC = q.popleft()
            remove += 1
            for n in adj[currC]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        return remove == numCourses
        
                