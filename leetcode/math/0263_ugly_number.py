class Solution:
    def isUgly(self, n: int) -> bool:
        h = [2,3,5]
        if n<=0:
            return False
        while True:
            if(n == 1):
                return True
            a = True
            for i in h:
                k = n/i
                if(k == int(k)):
                    n = k
                    a = False
                    break
            if a and n>1:
                return False
            
        