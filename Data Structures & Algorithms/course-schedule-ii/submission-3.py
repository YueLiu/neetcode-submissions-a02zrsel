class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # DAG
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        current_path = set()
        ans = []

        def dfs(c):
            if c in current_path:
                return False
            if preMap[c] == []:
                if c not in ans:
                    ans.append(c)
                return True
            
            current_path.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            ans.append(c)
            current_path.remove(c)
            preMap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return ans
            