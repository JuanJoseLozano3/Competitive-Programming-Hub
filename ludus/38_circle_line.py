n, m = map(int,input().split())
via = list(map(int,input().split()))

ade = [0]
atr = [0]

for i in range(n*2-1):
    i = i%n
    ade.append(ade[-1]+via[i])
#print(ade)
for i in range(m):
    uno,dos = map(int,input().split())
    suma1 = 0
    if(uno<dos):
        suma1 = min(ade[dos-1]-ade[uno-1],ade[n+uno-1]-ade[dos-1])
    elif(uno>dos):
        suma1 = min(ade[uno-1]-ade[dos-1],ade[n+dos-1]-ade[uno-1])
    print(suma1)
