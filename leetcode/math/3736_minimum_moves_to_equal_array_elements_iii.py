class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        c = 0
        for i in nums:
            c += m-i
        return c
        
