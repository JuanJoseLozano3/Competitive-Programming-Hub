class Solution:
    def digitSum(self, s: str, k: int) -> str:
        num = s
        while len(s)>k:
            num = ""
            t = ""
            n = len(s)%k
            for i in range(len(s)):
                if(i%k==0 and i != 0):
                    num += str(sum(list(map(int,list(t)))))
                    t = ""
                t += s[i]
            num += str(sum(list(map(int,list(t)))))
            s = num
        return num