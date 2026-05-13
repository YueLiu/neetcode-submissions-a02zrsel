class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)
            diff = s1 - s2
            if diff > 0:
                heapq.heappush(max_heap, -diff)
        max_heap.append(0)
        return -max_heap[0]

