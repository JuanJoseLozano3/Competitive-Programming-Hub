from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        stop = defaultdict(list)
        for bus in range(len(routes)):
            for parada in range(len(routes[bus])):
                stop[routes[bus][parada]].append(bus)

        cola = deque()
        cola.append(source)
        busesUsados = set()
        encontrado = False
        distancia = 0
        while cola:
            tam = len(cola)
            for _ in range(tam):
                parada = cola.popleft()
                if(parada == target):
                    encontrado = True
                    break
                for bus in stop[parada]:
                    if bus not in busesUsados:
                        busesUsados.add(bus)
                        for paraditas in routes[bus]:
                            cola.append(paraditas)
            if(encontrado):
                break
        
            distancia += 1

        if(encontrado):
            return distancia
        return -1