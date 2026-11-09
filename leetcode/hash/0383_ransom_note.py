from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = defaultdict(int)
        for i in ransomNote:
            dic1[i] += 1
        
        dic2 = defaultdict(int)
        for i in magazine:
            dic2[i] += 1
            
        for c,v in dic1.items():
            if(v > dic2[c]):
                return False
        return True