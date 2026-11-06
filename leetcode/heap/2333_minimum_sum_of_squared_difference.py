import heapq

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        heap = []
        ya = set()
        freq = {}

        for i in range(len(nums1)):
            res = abs(nums1[i] - nums2[i])

            if res not in ya:
                heapq.heappush(heap, -res)
                ya.add(res)

            freq[res] = freq.get(res, 0) + 1

        k = k1 + k2

        while heap and k > 0:
            mayor = -heapq.heappop(heap)
            ya.remove(mayor)

            if freq[mayor] == 0:
                continue

            if not heap:
                sigm = 0
            else:
                sigm = -heap[0]

            dif = mayor - sigm
            cant = freq[mayor] * dif

            if cant <= k:
                k -= cant

                frecuencia = freq[mayor]
                freq[mayor] = 0
                freq[sigm] = freq.get(sigm, 0) + frecuencia

                if sigm > 0 and sigm not in ya:
                    heapq.heappush(heap, -sigm)
                    ya.add(sigm)

            else:
                red = k // freq[mayor]
                sob = k % freq[mayor]
                may = mayor - red

                frecuencia = freq[mayor]
                freq[mayor] = 0

                if frecuencia - sob > 0:
                    freq[may] = freq.get(may, 0) + frecuencia - sob

                if sob > 0:
                    freq[may - 1] = freq.get(may - 1, 0) + sob

                k = 0

        suma = 0
        for valor, cantidad in freq.items():
            suma += valor**2 * cantidad

        return suma