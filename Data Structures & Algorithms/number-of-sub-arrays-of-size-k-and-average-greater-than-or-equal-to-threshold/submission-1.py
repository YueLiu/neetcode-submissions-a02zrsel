class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = sum_ = 0
        for r in range(len(arr)):
            sum_ += arr[r]
            if r >= k-1:
                res += sum_ >= threshold
                sum_ -= arr[r-k+1]
        return res