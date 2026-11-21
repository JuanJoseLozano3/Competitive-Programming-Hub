class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        if(n==1):
            return 1
        p = [[1],[1,1]]
        i = 2
        while i < n:
            e = [p[-1][0]*i%MOD]
            for j in range(1,i):
                v = (p[-1][j]*i+p[-1][j-1])%MOD
                e.append(v)
            e.append(1)
            p.append(e)
            i+=1
        return p[-1][k-1]