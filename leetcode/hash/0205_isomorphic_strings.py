
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = set()
        q = ""
        for i in range(len(s)):
            if s[i] not in dic1:
                if t[i] in dic2:
                    break
                q += t[i]
                dic1[s[i]] = t[i]
                dic2.add(t[i])
            else:
                q += dic1[s[i]]
        return q == t