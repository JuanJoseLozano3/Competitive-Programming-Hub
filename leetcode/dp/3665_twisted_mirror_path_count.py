from collections import defaultdict
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        def dfs(i,j,d):
            if ((i,j,d) in visitados):
                return visitados[(i,j,d)]

            if(i>fin[0] or j> fin[1]):
                return 0

            if((i,j) == fin):
                return 1
            
            c = 0
            
            if(grid[i][j]== 1):
                if(d == 0):
                    c += dfs(i+1,j,1)
                else:
                    c += dfs(i,j+1,0) 
            else:
                c += dfs(i,j+1,0)
                c += dfs(i+1,j,1)
            visitados[(i,j,d)] = c
            return c

        fin = (len(grid)-1,len(grid[0])-1)
        visitados = defaultdict(int)
        t = dfs(0,0,0)
        return t%(10**9+7)
