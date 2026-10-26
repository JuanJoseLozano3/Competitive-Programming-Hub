class Solution:
    def maxSumOfSquares(self, num: int, suma: int) -> str:
        falta = 0
        nu = ""
        k = suma
        while len(nu)<num:
            if(k>9):
                nu += "9"
                k -= 9
            else:
                nu += str(k)
                k = 0
        if(k!=0):
            return ""
        return nu
            