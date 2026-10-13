# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ini = 1
        fin = n
        mit = 1
        while ini<fin:
            mit = (ini+fin)//2
            
            if isBadVersion(mit):
                fin = mit
            else:
                ini = mit + 1
        return ini
        