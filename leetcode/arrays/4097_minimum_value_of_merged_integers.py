class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        nu = []
        for i in range(0,len(nums),2):
            nu.append(int(str(nums[i])+str(nums[i+1])))
        return min(nu)
            