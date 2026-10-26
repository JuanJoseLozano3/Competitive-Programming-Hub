class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        count = 0
        res = 0 
        for i, v in enumerate(nums): 
            if i != v:
                if count < 1: 
                    res = v
                else:
                    res &= v  
                count += 1 
        return res   
        
        

        