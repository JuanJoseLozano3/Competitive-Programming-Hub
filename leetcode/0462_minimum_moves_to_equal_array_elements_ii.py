class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums = sorted(nums)
        c = 0
        for i in range(len(nums)//2):
            c += (nums[len(nums)-1-i]-nums[i])
        return c
            
