class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for i, j, weight in edges:
            graph[i].append((j, weight))
        
        visited = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
        queue = []
        queue.append((0, 1, labels[0], 0))
        visited[0][1] = 0

        while queue:
            weight, curr_consecutive, last_letter, node = heapq.heappop(queue)
            if node == n - 1:
                return weight
            
            for next_node, edge_weight in graph[node]: 
                next_letter = labels[next_node]
                new_weight = weight + edge_weight
                next_consecutive = 1
                if last_letter == next_letter:
                    next_consecutive = curr_consecutive + 1
                
                if next_consecutive > k:
                    continue
                
                if visited[next_node][next_consecutive] <= new_weight:
                    continue
                
                visited[next_node][next_consecutive] = new_weight
                heapq.heappush(queue, (new_weight, next_consecutive, next_letter, next_node))
        
        return -1

        
