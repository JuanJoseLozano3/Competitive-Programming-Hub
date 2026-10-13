class Solution:
    def addDigits(self, num: int) -> int:
        k = str(num)
        while True:
            if(len(k)== 1):
                return int(k)
            suma = 0
            for i in k:
                suma += int(i)  
            k = str(suma)
        