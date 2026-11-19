from collections import defaultdict
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        graph = defaultdict(list)
        hab = 0
        for keys in rooms:
            for i in keys:
                graph[hab].append(i)
            hab +=1

        cola = deque()
        cola.append(0)
        visitados = set()
        t = [0]*len(rooms)
        distancia = 1
        while cola:
            tam = len(cola)
            for _ in range(tam):
                nodo = cola.popleft()
                t[nodo] = 1
                for hab in graph[nodo]:
                    if hab not in visitados:
                        visitados.add(hab)
                        cola.append(hab)
        j = t.count(0)
        return False if j > 0 else True
        