class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = []
        c = 0
        for i in nums:
            if i == 0:
                c += 1
                continue
            p.append(i)
        ze = [0]*c
        re = p+ze
        
        for i in range (len(re)):
            nums[i] = re[i]