class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        xy = 0
        yz = 0
        xz = [0]*50
        for i in grid:
            p = 0
            for j in i:
                xz[p] = max(xz[p],j)
                if(j>0):
                    xy += 1
                p+=1
            yz += max(i)
        return xy+yz+sum(xz)



        
        