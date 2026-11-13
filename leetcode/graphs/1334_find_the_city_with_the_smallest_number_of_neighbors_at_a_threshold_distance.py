from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        city = defaultdict(list)
        for u,v,w in edges:
            city[u].append((v,w))
            city[v].append((u,w))

        mejor = float("inf")
        cit = 0
        for i in range(n):
            cola = []
            heapq.heappush(cola, (0,i))
            vis = defaultdict(int)
            vis[i] = 0
            while cola:
                costo, nodo = heapq.heappop(cola)
                if(costo > distanceThreshold):
                    continue
                for voy, peso in city[nodo]:
                    nuevo = costo + peso
                    if nuevo > distanceThreshold:
                        continue
                    if(voy in vis and vis[voy] <= nuevo):
                        continue
                    vis[voy] = nuevo
                    heapq.heappush(cola, (nuevo,voy))

            if(mejor>=len(vis)-1):
                mejor = len(vis)-1
                cit = i
        
        return cit