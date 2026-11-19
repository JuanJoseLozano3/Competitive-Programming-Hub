class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        p = []
        for ini in range(len(nums)-l+1):
            for fin in range(ini+l-1, min(ini+r,len(nums))):
               val = sum(nums[ini:fin+1])
               #print(nums[ini],nums[fin])
               if(val>0):
                   p.append(val)
        
        return -1 if len(p)==0 else min(p)
        