n = int(input())
sumandoando=0
for i in range (n):
    b,c = map(int,input().split())
    sumandoando = max(sumandoando+c,b+c)
    print(sumandoando)