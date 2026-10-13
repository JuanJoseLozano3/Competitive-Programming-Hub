import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<0):
            return False
        
        n = bin(n)[2:]
        return n.count("1")==1