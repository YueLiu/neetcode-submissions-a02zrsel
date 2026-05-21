class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []      

    def addNum(self, num: int) -> None:
        # 大的分界线
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # 一开始都是小的，但是差距超过1就开始进大的
            heapq.heappush(self.small, -1* num)
        # 小的我们需要最大的在top，所以是* -1, 挪去大的时候要再 * -1
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1* heapq.heappop(self.small))
        # 大的我们本来就是最小的在top，所以挪去小的时候也要再 * -1才能保持在top
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def findMedian(self) -> float:
        # 不一样大说明奇数，直接返回多的第一个
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        # 偶数，各取一个求平均
        return (-1 * self.small[0] + self.large[0]) / 2