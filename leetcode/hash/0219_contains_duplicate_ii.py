class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        pos = 0
        for i in nums:
            if(i in dic):
                dic[i].append(pos)
            else:
                dic[i] = [pos]
            pos += 1
        
        for clave, valor in dic.items():
            if(len(valor)>1):
                for i in range(len(valor)):
                    for j in range(i+1,len(valor)):
                        if(abs(valor[i]-valor[j])<=k):
                            return True
        return False
                