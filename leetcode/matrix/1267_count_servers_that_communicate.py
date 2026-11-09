class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        ya = set()
        for i in range(len(grid)):
            c = 0
            p = []
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    c+= 1
                    p.append((i,j))
            if c > 1:
                for k in p:
                    ya.add(k)
        for i in range(len(grid[0])):
            c = 0
            p = []
            for j in range(len(grid)):
                if(grid[j][i]==1):
                    c+= 1
                    p.append((j,i))
            if c > 1:
                for k in p:
                    ya.add(k)
        return len(ya)
                    
        