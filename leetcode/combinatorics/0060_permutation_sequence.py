class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def next_permutation(nums):
           i = len(nums) - 2

           while i >= 0 and nums[i] >= nums[i + 1]:
              i -= 1

           if i >= 0:
              j = len(nums) - 1

              while nums[j] <= nums[i]:
                 j -= 1
 
              nums[i], nums[j] = nums[j],  nums[i]

           nums[i + 1:] = reversed(nums[i + 1:])
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        
 
        for i in range(k-1):
           next_permutation(nums)
        t = ""
        for i in range(len(nums)):
            t+=str(nums[i])
        return t
         