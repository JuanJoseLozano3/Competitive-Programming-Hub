class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        larven = k + 1
        inicio = 0
        ini = s[0:larven]
        for i in ini:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in range(larven, len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
            larven += 1
            if larven - max(dic.values()) > k:
                dic[s[inicio]] -= 1
                inicio += 1
                larven -= 1
        if(larven>=len(s)):
            return len(s)
        return larven
