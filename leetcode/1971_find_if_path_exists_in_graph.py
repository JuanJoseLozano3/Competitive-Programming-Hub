from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        def dfs(nodo):
            nonlocal resp
            if(nodo == destination):
                resp = True
                return 
            if(nodo in visitados):
                return 
            visitados.add(nodo)
            for i in graph[nodo]:
                dfs(i)
                if(resp == True):
                    return 

        resp = False
        visitados = set()
        dfs(source)
        return resp
