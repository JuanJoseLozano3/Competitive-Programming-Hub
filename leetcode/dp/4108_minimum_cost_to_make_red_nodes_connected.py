class Solution:
    def minCost(self, n: int, colors: str, edges: List[List[int]]) -> int:
        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        visited = set()
        sizes = [0] * n

        def dfs(curr=0):
            visited.add(curr)
            size = 1

            for son in tree[curr]:
                if son not in visited:
                    size += dfs(son)

            sizes[curr] = size
            return size

        dfs()

        dpr = [0] * n
        best = 0

        def dfs2(curr, parent):
            nonlocal best

            gain = 0
            if colors[curr] == 'R':
                gain = sizes[curr]
            else:
                gain = -sizes[curr]
                
            for son in tree[curr]:
                if son != parent:
                    dfs2(son, curr)
                    gain += max(0, dpr[son])

            dpr[curr] = gain
            best = max(best, gain)

        dfs2(0, -1)

        total = 0
        for i in range(n):
            if colors[i] == 'R':
                total += sizes[i]

        return total - best