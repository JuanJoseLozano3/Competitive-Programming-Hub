class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if(m == 1):
            return ["."*n]
        if(n==1):
            return ["."]*m
        f = []
        ini = "."*(n-1)+"#"
        f.append(ini)
        for i in range(m-2):
            ini = "#"*(n-2)+".#"
            f.append(ini)
        ini = "#"*(n-2)+".."
        f.append(ini)
        return f
