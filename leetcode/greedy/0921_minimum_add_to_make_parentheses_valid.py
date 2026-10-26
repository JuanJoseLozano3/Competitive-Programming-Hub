class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        t = 0
        for i in s:
            if(i == "("):
                stack+= 1
            else:
                stack -= 1
                if(stack < 0):
                    t += 1
                    stack += 1
        t += stack
        return t
        
