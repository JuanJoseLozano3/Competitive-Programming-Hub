from collections import defaultdict 

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1 = defaultdict(int)
        for i in s:
            dic1[i] += 1
        dic2 = defaultdict(int)
        for i in t:
            dic2[i] += 1
            
        for c,v in dic2.items():
            if v != dic1[c]:
                return c
        
        