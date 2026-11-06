class Solution:
    def minMoves(self, nums: list[int]) -> int:
        men = min(nums)
        diff = 0
        for i in range(len(nums)-1,-1,-1):
            diff += nums[i]-men
        return diff
