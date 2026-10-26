class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        f = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                p = len(set(nums[i:j+1]))
                f += p**2
        return f