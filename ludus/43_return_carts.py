n, w = map(int,input().split())
b = list(map(int,input().split()))
b = sorted(b)
c = 0

ini = 0
fin = n-1
while ini<=fin:
    su = b[ini]+b[fin]
    if(su<=w):
        ini += 1
    c+=1
    fin -= 1
print(c)