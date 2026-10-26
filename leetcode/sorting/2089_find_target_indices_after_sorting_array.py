class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        f = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if(nums[i]==target):
                f.append(i)
        return f
            
        