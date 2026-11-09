class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        c = 0
        p = 0
        n = len(nums)
        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    c += 1
                    if(locked[j] == 1):
                        c+= 1
                        locked[j] = 0
                        p+=1
                    if(locked[j+1] == 1):
                        c+= 1
                        locked[j+1] = 0
                        p+=1
                if(p>k):
                    return -1
        return c
        