class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        tam = len(bloomDay)
        if(tam<(m*k)):
            return -1
        izq= min(bloomDay)
        der = max(bloomDay)

        while(izq <= der):
            mitad = (der+izq)//2
            cont = 0
            ramos = 0
            for i in range(len(bloomDay)):
                if(bloomDay[i]<=mitad):
                    cont += 1
                else:
                    cont = 0
                if(cont == k):
                    ramos+=1
                    cont = 0
            if(ramos >= m):
                der = mitad - 1
            else:
                izq = mitad + 1
        return izq

            
            
            
        
        
