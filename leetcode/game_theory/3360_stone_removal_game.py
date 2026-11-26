class Solution:
    def canAliceWin(self, n: int) -> bool:
        a = False
        for i in range(10,-1,-1):
            n-=i
            
            if(n<0):
                return a
            a = not(a)
        return a
        
        