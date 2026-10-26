class Solution:
    def decodeString(self, s: str) -> str:
        n = set(["0","1","2","3","4","5","6","7","8","9"])
        stack = []
        sal = ""
        for i in range(len(s)):
            if(s[i]=="["):
                stack.append(len(sal))
            elif(s[i]=="]"):
                num = ""
                j = stack[-1]-1
                while j>-1:
                    if(sal[j] not in n):
                        break
                    num += sal[j]
                    j -= 1
                p = len(num)
                num = int(num[::-1])
                lar = sal[stack[-1]+1:]
                pal = lar*num
                sal = sal[:len(sal)-len(lar)-1-p]+pal
                stack.pop()
                continue
            sal+=s[i]
        return sal

        