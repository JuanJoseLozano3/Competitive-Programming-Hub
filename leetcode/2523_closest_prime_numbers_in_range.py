class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:

        def criba(n):
            primos = [True]*n

            if n > 0:
                primos[0] = False
            if n > 1:
                primos[1] = False

            i = 2
            while i*i < n:
                if primos[i]:
                    j = i*i
                    while j < n:
                        primos[j] = False
                        j += i
                i += 1

            l = []
            for i in range(n):
                if (primos[i] and i>= left):
                    l.append(i)
            print(l)
            return l
            
        f = criba(right+1)
        p = []
        m = float("inf")
        for i in range(1,len(f)):
            if(f[i]-f[i-1] < m):
                p = [f[i-1], f[i]]
                m = f[i]-f[i-1]
        if(len(f)<=1):
            return [-1,-1]
        return p