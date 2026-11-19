from collections import defaultdict
import heapq

class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        graph = defaultdict(list)
        reversedGraph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            reversedGraph[v].append((u, w))

        def dijkstra(source, graph):
            heap = []
            heapq.heappush(heap, (0, source))

            dist = [float('inf')] * n
            dist[source] = 0

            while len(heap) > 0:
                currW, node = heapq.heappop(heap)

                if currW > dist[node]:
                    continue

                for vec, w in graph[node]:
                    newW = currW + w

                    if newW < dist[vec]:
                        dist[vec] = newW
                        heapq.heappush(heap, (newW, vec))

            return dist

        d1 = dijkstra(src1, graph)
        d2 = dijkstra(src2, graph)
        d3 = dijkstra(dest, reversedGraph)

        ans = float('inf')

        for i in range(n):
            if d1[i] != float('inf') and d2[i] != float('inf') and d3[i] != float('inf'):
                ans = min(ans, d1[i] + d2[i] + d3[i])

        if ans == float('inf'):
            return -1

        return ans