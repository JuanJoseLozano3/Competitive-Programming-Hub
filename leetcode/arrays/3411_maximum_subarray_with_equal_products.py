import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        t = len(nums)
        f = []
        for i in range(t):
            gcd = nums[i]
            lcm = nums[i]
            mult = nums[i]
            for j in range(i+1,t):
                gcd = math.gcd(gcd,nums[j])
                lcm = math.lcm(lcm,nums[j])
                mult *= nums[j]
                #print(nums[i],nums[j],gcd,lcm,mult)
                if (mult == gcd*lcm):
                    f.append(j-i)
        return max(f)+1
                
