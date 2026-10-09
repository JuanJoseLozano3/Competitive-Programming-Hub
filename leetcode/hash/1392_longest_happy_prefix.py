class Solution:
    def longestPrefix(self, s: str) -> str:
        letras = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
            'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
            'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26
        }
        base = 27
        mod = 10**9 + 7
        n = len(s)
        hash_s = 0
        hash_rev = 0
        mas = -1
        for i in range(n-1):
            hash_s = (hash_s + letras[s[i]] * pow(base,i,mod))%mod
            hash_rev = ((base*hash_rev)%mod + letras[s[n-1-i]])%mod

            if(hash_s == hash_rev):
                mas = i

        if(mas == -1):
            return ""
        else:
            return s[0:mas+1]
