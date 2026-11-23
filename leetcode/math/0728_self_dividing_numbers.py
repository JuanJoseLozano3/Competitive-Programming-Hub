class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        f = []
        for i in range(left,right+1):
            num = str(i)
            c = 0
            for j in num:
                val = int(j)
                if(val == 0):
                    continue
                if(i%val==0):
                    c+=1
            if(c==len(num)):
                f.append(i)
        return f