class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for pair in points:
            distance = (pair[0]**2 + pair[1]**2)**0.5
            heapq.heappush(q, [-distance, pair[0], pair[1]])
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        for i in q:
            ans.append(i[1:])
        return ans 