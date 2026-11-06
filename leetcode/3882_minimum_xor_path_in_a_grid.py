class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        mi = float("inf")
        def dfs(i,j,costo):
            nonlocal mi
            if(i>=len(grid) or j>=len(grid[0])):
                return 
            costo ^= grid[i][j]
            if(i == len(grid)-1 and j == len(grid[0])-1):
                bit = 1 << costo
                val[i][j] |= bit
                if(costo<mi):
                   mi = costo
                return 
            
            if val[i][j] & (1 << costo):
                return
            
            bit = 1 << costo
            val[i][j] |= bit
            dfs(i+1,j,costo)
            dfs(i,j+1,costo)
        
        val = []
        for i in range(len(grid)):
            val.append([0]*len(grid[0]))
        
        dfs(0,0,0)
        return mi
         
