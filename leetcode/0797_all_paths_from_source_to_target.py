class Solution:
    def allPathsSourceTarget(self, con: list[list[int]]) -> list[list[int]]:
        graph = {}
        t = len(con)
        for i in range(t):
            graph[i] = con[i]

        def dfs(nodo):
            visitados.append(nodo)
            if(nodo == t-1):
                f.append(visitados.copy())
                visitados.pop()
                return 
            for i in graph[nodo]:
                dfs(i)
            visitados.pop()

        f = []
        visitados = []
        dfs(0)
        return f
