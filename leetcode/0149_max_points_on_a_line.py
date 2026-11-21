from collections import defaultdict
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        dic = defaultdict(set)
        t = len(points)
        for i in range(t):
            for j in range(i+1,t):
                num = points[j][1]-points[i][1]
                den = points[j][0]-points[i][0]
                if(den != 0):
                    m = num/den
                    b = points[i][1]-m*points[i][0]
                else:
                    m = float("inf")
                    b = points[i][0]
                
                dic[(m,b)].add(i)
                dic[(m,b)].add(j)
        ma = 1
        for clave,valor in dic.items():
            ma = max(len(valor),ma)
        
        return ma
