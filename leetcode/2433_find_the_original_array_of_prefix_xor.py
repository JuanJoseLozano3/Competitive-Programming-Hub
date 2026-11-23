class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        f = [pref[0]]
        for i in range(1,len(pref)):
            f.append(pref[i-1]^pref[i])
        return f