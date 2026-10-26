class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def dfs(j, i, isla):
            if ((j,i) in isla or i == len(grid[0]) or j == len(grid) or i == -1 or j == -1 or grid[j][i] == 0):
                return 0
            isla.add((j,i))
            suma = grid[j][i]
            suma += dfs(j, i+1, isla)
            suma += dfs(j, i-1, isla)
            suma += dfs(j+1, i, isla)
            suma += dfs(j-1, i, isla)
            
            return suma
            
        isla = set()
        cont = 0
        dicIslas = {}
        for p in range(len(grid)):
            for q in range(len(grid[0])):
                if(grid[p][q] != 0 and (p,q) not in isla):
                    suma = dfs(p,q,isla)
                    if( suma%k==0):
                        cont += 1
                     
        return cont
        
        