class Solution:
    def reverse(self, x: int) -> int:
        t = str(x)
        flag = False
        if(t[0]=="-"):
            flag = True
            t=t[1::]
        t = int(t[::-1])
        if(flag):
            t*=-1
        if(t<-2**31 or t>2**31-1):
            return 0
        return(t)