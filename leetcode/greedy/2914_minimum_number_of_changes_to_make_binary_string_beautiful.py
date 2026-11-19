from collections import defaultdict
class Solution:
    def minChanges(self, s: str) -> int:
        dic = defaultdict(int)
        dic[s[0]] += 1
        change = 0
        for i in range(1,len(s)):
            if(s[i] in dic):
                dic[s[i]] += 1
            else:
                if((i-1)%2==1):
                    change += min(dic["0"],dic["1"])
                    dic = defaultdict(int)
                    dic[s[i]] += 1
                else:
                    dic[s[i]] += 1
                    change += min(dic["0"],dic["1"])
                    dic = defaultdict(int)
                    dic[s[i]] = 0
        return change



        