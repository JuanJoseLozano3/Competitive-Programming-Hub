from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        mejor = float("inf")
        lis = [-1]*n
        cola = []
        heapq.heappush(cola, (0,k))
        vis = defaultdict(int)
        vis[k] = 0
        lis[k-1] = 0
        while cola:
            costo, nodo = heapq.heappop(cola)
            for voy, peso in graph[nodo]:
                nuevo = costo + peso
                if(voy in vis and vis[voy] <= nuevo):
                    continue
                vis[voy] = nuevo
                heapq.heappush(cola, (nuevo,voy))
                lis[voy-1] = nuevo  

        ma = 0
        mi = float("inf")
        for i in lis:
            if(i>ma):
                ma = i
            if(i<mi):
                mi = i
        if(mi == -1):
            return -1
        return ma