n, l = map(int,input().split())
val = []
for i in range(n):
    sal, lle = map(int,input().split())
    if(sal >= l):
        val.append(lle)

if(len(val) == 0):
    print(-1)
else:
    print(min(val))