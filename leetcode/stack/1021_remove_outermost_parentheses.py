class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = 1
        ini = 0
        res = ""
        for i in range(1,len(s)):
            if(s[i]=="("):
                stack +=1
            else:
                stack -=1
            
            if(stack == 0):
                res += s[ini+1:i]
                ini = i+1
        return res
