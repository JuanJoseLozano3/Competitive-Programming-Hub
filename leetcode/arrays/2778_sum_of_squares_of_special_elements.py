class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        suma = 0
        for i in range(n):
            if(n%(i+1)==0):
                suma += (nums[i]**2)
                
        return suma
            
        