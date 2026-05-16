class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # math trick
        # (maxFreq - 1)(n+1) + maxFreqCount
        count = [0]*26
        for task in tasks:
            index = ord(task) - ord("A")
            count[index] += 1
        maxFreq = max(count) #O(n)
        maxFreqCount = 0
        for i in count:
            if i == maxFreq:
                maxFreqCount += 1
        
        return max(((maxFreq - 1)*(n+1) + maxFreqCount), len(tasks))
        