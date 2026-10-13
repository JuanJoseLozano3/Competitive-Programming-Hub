
import heapq

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        tam = len(nums)
        menores = []
        mayores = []
        for i in range(tam):
            valor = nums[i] ** 2
            heapq.heappush(menores, valor)
            heapq.heappush(mayores, -valor)

        suma = 0
        if tam % 2 == 0:
            for i in range(tam // 2):
                valor = heapq.heappop(menores)
                suma -= valor
            for i in range(tam // 2):
                valor = heapq.heappop(mayores)
                suma += -valor
        else:
            for i in range(tam // 2):
                valor = heapq.heappop(menores)
                suma -= valor
            for i in range(tam // 2 + 1):
                valor = heapq.heappop(mayores)
                suma += -valor
        return suma