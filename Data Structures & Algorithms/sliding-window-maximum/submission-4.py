
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()

        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if i+1-k > dq[0]:
                dq.popleft()

            if (i + 1) >= k:
                ans.append(nums[dq[0]])
        return ans




