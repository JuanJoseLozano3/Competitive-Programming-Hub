class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        dic = {}
        c = 0 
        t = len(arr2)
        for i in arr1:
            if(i in dic):
                c+= dic[i]
                continue
            p = 0
            for j in arr2:
                if(abs(i-j)>d):
                    p+=1
            if(p==t):
                dic[i] = 1
                c += 1
            else:
                dic[i] = 0
        return c

            
        
