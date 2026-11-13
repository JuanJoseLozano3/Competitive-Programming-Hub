class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        resp = 1
        men = 0
        may = 0
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                resp = max(resp,i-may+1)
            else:
                may = i
            if(nums[i]<nums[i-1]):
                resp = max(resp,i-men+1)
            else:
                men = i
        return resp
        