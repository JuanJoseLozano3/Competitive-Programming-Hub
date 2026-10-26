class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sal = "0"
        for i in range(n):
            inv = int(sal[::-1], 2)
            lim = int("1" * len(sal), 2)
            agrego = (~inv) & lim
            sal += "1"+format(agrego, f"0{len(sal)}b")
        return sal[k-1]