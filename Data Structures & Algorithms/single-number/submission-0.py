class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort in-place; do not assign to a variable
        # Step through the list in increments of 2
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1] # The single number is the last one if no mismatch found
