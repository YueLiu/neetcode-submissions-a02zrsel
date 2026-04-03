class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles) # this is speed range
        ans = r
        while l <= r:
            rate = l + (r-l)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/rate)
            if total_time <= h:
                r = rate - 1
                ans = rate
            else:
                l = rate + 1

        return ans
                
