class Solution:
    def isHappy(self, n: int) -> bool:
        l = set()
        k = n
        while k!= 1:
            if(k in l):
                return False
            l.add(k)
            suma = 0
            for i in str(k):
                suma += int(i)**2
            k = suma
            
        return True