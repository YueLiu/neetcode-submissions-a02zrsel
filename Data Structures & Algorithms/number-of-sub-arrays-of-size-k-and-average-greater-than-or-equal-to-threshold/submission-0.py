class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix_sum = [0]*(len(arr)+1)
        for i in range(len(arr)):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]

        res = l = 0
        for r in range(k-1, len(arr)):
            sum_ = prefix_sum[r+1] - prefix_sum[l]
            if sum_/k >= threshold:
                res += 1
            l +=1
        return res