class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = list(pattern)
        m = s.split()
        if(len(h) != len(m)):
            return False
        usadas = set()
        dic = {}
        for i in range(len(m)):
            if(m[i] in dic):
                if(dic[m[i]] != h[i]):
                    return False
            else: 
                dic[m[i]] = h[i]
                if(h[i] not in usadas):
                    usadas.add(h[i])
                else:
                    return False
        return True
        