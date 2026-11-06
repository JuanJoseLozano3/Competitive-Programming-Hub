class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        m = [0]*n
        for i in edges:
            m[i[1]] += 1
        res = []
        for i in range(n):
            if(m[i]==0):
                res.append(i)
        return res
