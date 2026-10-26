import heapq
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        heap = []
        pos = 0
        pe = {}
        for i in nums:
            h = str(i)
            suma = 0
            for j in h:
                suma += int(j)
            heapq.heappush(heap, (suma, i, pos))
            pos+=1
        swap = 0
        p = 0
        while heap:
            x = heapq.heappop(heap)
            if x[1] in pe and x[2] != pe[x[1]]:
                x = [x[0], x[1], pe[x[1]]]
                
            if x[1] != nums[p]:
                swap += 1
                aux = nums[p]
                nums[x[2]] = aux
                pe[aux] = x[2]
                pe[x[1]] = p
            
            p += 1
        return swap
            
