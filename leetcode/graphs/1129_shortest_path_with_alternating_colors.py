from collections import defaultdict
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for i in redEdges:
            graph[i[0]].append((i[1],False))
        for i in blueEdges:
            graph[i[0]].append((i[1],True))

        cola = deque()
        colaC = deque()
        cola.append(0)
        colaC.append(None)
        visitados = set()

        t = [-1]*n

        t[0] = 0

        distancia = 1

        while cola:
            tam = len(cola)

            for _ in range(tam):
                nodo = cola.popleft()
                color = colaC.popleft()
        
                for vecinos in graph[nodo]:
                    if vecinos not in visitados and color != vecinos[1]:
                        visitados.add(vecinos)

                        colaC.append(vecinos[1])
                        cola.append(vecinos[0])
                        if t[vecinos[0]] == -1:
                            t[vecinos[0]] = distancia
            distancia += 1


        return t
        
