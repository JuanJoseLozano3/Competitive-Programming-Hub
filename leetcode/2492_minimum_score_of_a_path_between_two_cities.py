from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list)
        pesos = defaultdict(list)
        for i in range(len(roads)):
            graph[roads[i][0]].append(roads[i][1])
            graph[roads[i][1]].append(roads[i][0])
            pesos[roads[i][0]].append(roads[i][2])

        def dfs(nodo):
            if(nodo in visitados):
                return
            visitados.add(nodo)
            for i in graph[nodo]:
                dfs(i)

        f = []
        visitados = set()
        dfs(1)
        for i in visitados:
            f += pesos[i]      
        return min(f)
