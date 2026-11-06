class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        v = 0
        ta = len(s)
        if ta == 0:
            return True
        if(len(t) == 0):
            return ta==0
        for i in range(len(t)):
            if(s[v] == t[i]):
                v+= 1
            if(v==ta):
                break
        return v==ta

        
        
