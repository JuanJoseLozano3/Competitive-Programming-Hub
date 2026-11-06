from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        def dfs(nodo):
            if(nodo in visitados):
                return
            if(nodo not in visitados):
                reino.append(nodo)
            visitados.add(nodo)
            for i in graph[nodo]:
                dfs(i)

        f = 0
        visitados = set()
        for i in range(n):
            if(i not in visitados):
                reino = []
                dfs(i)
                t = len(reino)
                ca = 0
                for i in reino:
                    if(len(graph[i]) == t-1):
                        ca+=1
                if(ca == t):
                    f+=1
        return f
