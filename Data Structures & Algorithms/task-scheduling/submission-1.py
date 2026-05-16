class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for task in tasks:
            index = ord(task)-ord("A")
            count[index] += 1
        maxHeap = [-i for i in count if i > 0]
        heapq.heapify(maxHeap)

        q = deque() #(freq, nextTime)

        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                remainingCount = heapq.heappop(maxHeap) + 1 #负数
                if remainingCount < 0:
                    q.append((remainingCount, time + n))
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
