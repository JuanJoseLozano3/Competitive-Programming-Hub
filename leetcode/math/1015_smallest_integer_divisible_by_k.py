class Solution:
    def smallestRepunitDivByK(self, k):
        p = str(k)
        if(p[-1] != "1" and p[-1] != "3" and p[-1] != "7" and p[-1] != "9"):
            return -1
        t = 0
        for i in range(10**5):
            t = t*10 + 1
            if(t%k == 0):
                return i+1
        return -1