class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProduct = {}
        product = 1
        for i in range(len(nums)):
            product = product * nums[i]
            prefixProduct[i] = product
        
        postProduct = {}
        product = 1
        for i in reversed(range(len(nums))):
            product = product * nums[i]
            postProduct[i] = product      

        ans = []
        ans.append(postProduct[1])
        for i in range(1, len(nums)-1):
            ans.append(prefixProduct[i-1] * postProduct[i+1])
        ans.append(prefixProduct[len(nums)-2])

        return ans

            
  

        
