class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for u,v,w in edges:
            self.graph[u].append((v,w))

    def addEdge(self, edge: list[int]) -> None:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        self.graph[u].append((v,w))
        return -1
        

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = []
        heapq.heappush(heap, (0, node1))

        dist = [float('inf')] * self.n
        dist[node1] = 0

        while len(heap) > 0:
            currW, node = heapq.heappop(heap)

            if currW > dist[node]:
                continue

            if(node == node2):
                return currW

            for vec, w in self.graph[node]:
                newW = currW + w

                if newW < dist[vec]:
                    dist[vec] = newW
                    heapq.heappush(heap, (newW, vec))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)