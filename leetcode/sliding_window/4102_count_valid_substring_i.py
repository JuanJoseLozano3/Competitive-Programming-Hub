class Solution:
    def countValidSubstrings(self, s: str) -> int:
        c = 0
        ini = 0
        fin = 0
        ven = []
        n = ["a","b","c"]
        pos = 0
        for i in range(len(s)):
            if(s[i] == n[pos]):
                pos += 1
            else:
                pos = 0
                if(s[i] == n[pos]):
                    pos += 1
            if(pos == 3):
                k = (fin-ini)
                c += (k*(k+1))//2 - 1
                pos = 0
                ini = fin-1
            fin += 1
        k = fin-ini
        c += (k*(k+1))//2
        
        return c
            