class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        mas = 0
        for i in s:
            if(i == "("):
                stack.append(i)
            elif(i==")"):
                mas = max(mas,len(stack))
                stack.pop()
        return mas
            
        