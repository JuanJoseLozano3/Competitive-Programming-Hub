class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def dfs(j, i, isla):
            if ((j,i) in isla or i == len(grid[0]) or j == len(grid) or i == -1 or j == -1 or grid[j][i] == 1):
                return
            isla.add((j,i))
            dfs(j, i+1, isla)
            dfs(j, i-1, isla)
            dfs(j+1, i, isla)
            dfs(j-1, i, isla)
            
        isla = set()
        cont = 0
        dicIslas = {}
        for p in range(len(grid)):
            for q in range(len(grid[0])):
                if(grid[p][q] != 1 and (p,q) not in isla):
                    t = len(isla)
                    a = isla.copy()
                    dfs(p,q,isla)
                    if(len(isla) != t):
                        cont += 1
                        dicIslas[cont] = isla - a

        
        cont = 0
        for clave,valor in dicIslas.items():
            c = 0
            for v in valor:
                if(v[0] == 0 or v[0]==len(grid)-1 or v[1] == 0 or v[1]==len(grid[0])-1):
                    c+= 1
            if(c == 0):
                cont+=1
        return cont
        
        