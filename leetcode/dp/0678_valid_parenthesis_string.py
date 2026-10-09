class Solution:
    def checkValidString(self, s: str) -> bool:
        
        memo = {}

        def rec(stack, pos):
            
            if stack < 0:
                return -1

            if (stack, pos) in memo:
                return memo[(stack, pos)]

            if pos == len(s):
                return 0 if stack == 0 else -1

            v,v1,v2,v3 = -1,-1,-1,-1

            if(s[pos] == "("):
                v = rec(stack+1, pos+1)

            elif(s[pos] == ")"):
                v = rec(stack-1, pos+1)

            else:
                v1 = rec(stack+1, pos+1)
                v2 = rec(stack-1, pos+1)
                v3 = rec(stack, pos+1)

            if(v == 0 or v1 == 0 or v2 == 0 or v3 == 0):
                memo[(stack, pos)] = 0
                return 0

            memo[(stack, pos)] = -1
            return -1

        return rec(0, 0) == 0
