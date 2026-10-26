class Solution:
    def minInsertions(self, s: str) -> int:
        sa = ""
        ant = 0
        for i in s:
            if(i == "("):
                if(ant == 1):
                    sa += "."
                    ant = 0
                sa += "("
            elif(ant == 1):
                sa += ")"
                ant = 0
            else:
                ant = 1
        if(ant == 1):
            sa += "."
            ant = 0
        
        stack = 0
        mi = 0
        for i in sa:
            if(i == "("):
                stack += 1
            elif(i == ")"):
                stack -= 1
            else:
                stack -= 1
                mi += 1
            if(stack < 0):
                mi+= 1
                stack += 1
        if(stack > 0):
            mi += stack*2
        return mi
            
        
