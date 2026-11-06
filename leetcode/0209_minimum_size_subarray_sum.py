class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ini = 0
        suma = nums[0]
        if(suma >= target):
            return 1
        fin = 1
        f = float("inf")
        st = True
        while fin < len(nums):
            if st:
                suma += nums[fin]
            if(suma == target):
                print(ini, fin)
                f = min(f,fin-ini+1)
                fin += 1
                st = True
            elif(suma > target):
                
                f = min(f,fin-ini+1)
                suma -= nums[ini]
                ini += 1
                st = False
            else:
                fin += 1
                st = True
        if(f == float("inf")):
            return 0
        return f
            
