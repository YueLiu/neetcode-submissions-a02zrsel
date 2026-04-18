class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # DAG
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        current_path = set()

        def dfs(c):
            if c in current_path:
                return False
            if preMap[c] == []:
                return True
            
            current_path.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            current_path.remove(c)
            preMap[c] = []
            return True

        for c in range(len(prerequisites)):
            if not dfs(c):
                return False
        return True


