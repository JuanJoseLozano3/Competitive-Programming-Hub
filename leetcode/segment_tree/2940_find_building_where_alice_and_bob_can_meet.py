class Solution:
    class SegmentTree:
        def __init__(self, nums: list[int]):
            self.n = len(nums)
            self.tree = [0]*(2*self.n)
            for i in range(self.n):
                self.tree[self.n+i] = nums[i]
            
            for i in range(self.n-1,0,-1):
                self.tree[i] = max(self.tree[2*i],self.tree[2*i+1])

        def maxRange(self, left: int, right: int, parada: int) -> int:
            left += self.n
            right += self.n + 1

            izq = []
            der = []

            while left < right:
                if left % 2:
                    izq.append(left)
                    left += 1

                if right % 2:
                    right -= 1
                    der.append(right)

                left //= 2
                right //= 2

            candidatos = izq + der[::-1]
            for nodo in candidatos:
                if self.tree[nodo] > parada:
                    while nodo < self.n:
                        if self.tree[nodo*2] > parada:
                            nodo *= 2
                        else:
                            nodo = nodo*2+1
                    pos = nodo-self.n

                    if pos >= (left_original := 0): 
                        return pos
            return -1

    def leftmostBuildingQueries(self, heights, queries):
        k = self.SegmentTree(heights)
        final = []

        for a, b in queries:
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                final.append(b)
            else:
                final.append(k.maxRange(b+1, k.n-1, heights[a]))

        return final
        


