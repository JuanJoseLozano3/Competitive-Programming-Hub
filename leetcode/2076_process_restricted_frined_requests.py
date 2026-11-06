class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            nonlocal parent
            ra = find(a)
            rb = find(b)
            if ra != rb:
                p = parent.copy()               
                parent[rb] = ra
                c = False
                for rest in restrictions:
                    if(find(rest[0]) == find(rest[1])):
                        c = True
                        break
                if(c):
                    parent = p
                    return False
                else:
                    return True   
            else:
                c = False
                for rest in restrictions:
                    if(find(rest[0]) == find(rest[1])):
                        c = True
                        break
                if(c):
                    return False
                else:
                    return True   

        
        parent = []
        for i in range(n):
            parent.append(i)
        
        res = []
        for pre in requests:
            res.append(union(pre[0],pre[1]))
    
        return res
            
                
