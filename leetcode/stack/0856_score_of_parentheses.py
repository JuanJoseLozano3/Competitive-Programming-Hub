class Solution:
    def scoreOfParentheses(self, s: str) -> int:        
        stack = []
        res = 0
        for i in s:
            if(i == "("):
                stack.append(res)
                res = 0
            else:
                res = stack.pop() + max(res*2, 1)
        return res


