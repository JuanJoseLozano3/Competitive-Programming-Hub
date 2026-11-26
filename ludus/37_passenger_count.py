n = int(input())
f = []
suma = 0
for i in range(n):
    sa, en = map(int,input().split())
    suma += (en-sa)
    f.append(suma)
ma = max(f)
p = 0
j = f.index(ma)
print(ma,j+1)