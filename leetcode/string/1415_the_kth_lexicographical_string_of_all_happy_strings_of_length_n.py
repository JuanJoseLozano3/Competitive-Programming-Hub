class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        suman = 2**(n-1)
        if(k > suman*3):
            return ""
        k -= 1
        t = n-1
        f = ""
        i = {0: "a", 1: "b", 2:"c", 3:"c"}
        res = k//(2**(t))
        f+=i[res]
        i1 = {"a": {0:"b", 1: "c"},"b": {0:"a", 1: "c"},"c": {0:"a", 1: "b"}}
        while len(f)<n:
            k = k%(2**(t))
            t-=1
            res = k//(2**(t))
            f+=i1[f[-1]][res]
        return f