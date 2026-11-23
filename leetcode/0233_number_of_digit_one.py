class Solution:
    def countDigitOne(self, n: int) -> int:
        k = str(n)
        t = len(k)
        suma = 0
        for i in range(t):
            factor = 10**(t-i-1)
            if(i>0):
                h = int(k[:i])
            else:
                h = 0
            c = int(k[i])
            if(i+1<t):
                l = int(k[i+1:])
            else:
                l = 0
            if c > 1:
                suma += (h*factor + factor)
            elif(c == 1):
                suma += (h*factor + l+1)
            else:
                suma += h*factor
        return suma
        