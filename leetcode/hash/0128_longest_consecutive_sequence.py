class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        def dfs(val):
            if(val in apa):
                return apa[val]
            if(val not in nu):
                return 0
            apa[val] = 1 + dfs(val + 1)
            return apa[val]

        nu = set(nums)        
        ma = 0
        apa = {}

        for val in nu:
            dfs(val)
            if(apa[val]>ma):
                ma = apa[val]
            
        return ma

            
        
