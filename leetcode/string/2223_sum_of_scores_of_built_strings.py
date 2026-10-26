
class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        dpZ = [0] * n
        l = 0
        r = 0
        mov = 0
        suma = 0
        i = 1
        while i < n:
            if s[i] == s[l]:
                l = i
                r = i
                j = i
                while j < n and r < n:
                    if(s[j] == s[r-l]):
                        r += 1
                        j += 1
                    else:
                        break
                dpZ[i] = r - l
                suma += dpZ[i]
                i += 1
                while i < j:
                    dpZ[i] = min(dpZ[i-l], r-i)

                    while i + dpZ[i] < n and s[dpZ[i]] == s[i + dpZ[i]]:
                        dpZ[i] += 1

                    suma += dpZ[i]
                    i += 1
                i -= 1
            else:
                dpZ[i] = 0
            i += 1
        return suma + n
