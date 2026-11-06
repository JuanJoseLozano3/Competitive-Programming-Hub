class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        n = len(values)
        graph = [[] for _ in range(n)]
        
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        visited = [0] * n
        ans = 0
        
        def dfs(node, time, score):
            nonlocal ans
            
            if time > maxTime:
                return
            
            if visited[node] == 0:
                score += values[node]
            
            visited[node] += 1
            
            if node == 0:
                ans = max(ans, score)
            
            for nei, cost in graph[node]:
                dfs(nei, time + cost, score)
            
            visited[node] -= 1
        
        dfs(0, 0, 0)
        return ans
