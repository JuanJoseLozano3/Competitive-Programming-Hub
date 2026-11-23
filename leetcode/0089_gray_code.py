class Solution:
    def grayCode(self, n: int) -> list[int]:
        nums = []
        for i in range(2**n):
            k = [0]*n
            nums.append(k)

        c0 = "0"
        c1 = "1"
        for i in range(n):
            rep = c0*2**i+c1*2**i
            p = 0
            re = 0
            while p<2**n:
                nums[p][n-i-1] = rep[re]
                re += 1 
                if(re==2**i+2**i):
                    rep = rep[::-1]
                    re = 0
                p += 1
        f = []
        for i in nums:
            f.append(int(''.join(i),2))
        return f
