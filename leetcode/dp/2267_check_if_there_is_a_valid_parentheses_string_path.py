class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        ancho = len(grid)-1
        largo = len(grid[0])-1

        def dp(m,n,stack,memo):

            key = str(m)+str(n)+str(stack)

            if(key in memo):
                return memo[key]

            var = False

            if(m == ancho and n == largo and grid[m][n] == ")"):
                stack -= 1

                if(stack < 0):
                    memo[key] = False
                    return False

                if(stack == 0):
                    memo[key] = True
                    return True

            if(grid[m][n] == ")"):
                stack -= 1

                if(stack < 0):
                    memo[key] = False
                    return False

                if(m < ancho):
                    var = dp(m+1,n,stack,memo)
                    if(var == True):
                        memo[key] = True
                        return True

                if(n < largo):
                    var = dp(m,n+1,stack,memo)
                    if(var == True):
                        memo[key] = True
                        return True

            elif(grid[m][n] == "("):
                stack += 1

                if(m < ancho):
                    var = dp(m+1,n,stack,memo)
                    if(var == True):
                        memo[key] = True
                        return True

                if(n < largo):
                    var = dp(m,n+1,stack,memo)
                    if(var == True):
                        memo[key] = True
                        return True

            else:
                return False

            memo[key] = var
            return var


        if(grid[0][0] == ")" or grid[ancho][largo] == "("):
            return False

        stack = 0
        memo = {}

        var = dp(0,0,stack,memo)

        return var