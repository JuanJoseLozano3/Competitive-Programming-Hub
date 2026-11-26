n,m = map(int,input().split())
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra
        return True
    return False

for i in range(m):
    p,s = map(int,input().split())
    union(p-1, s-1)

grupos = set()
for i in range(n):
    grupos.add(find(i))
print(len(grupos))