i,j = map(int,input().split())
mapa = []
for _ in range(i):
    fi = input()
    l = []
    for k in fi:
        l.append(k)
    mapa.append(l)

f = 0
dx = [1,-1,0,0,0]
dy = [0,0,1,-1,0]

for y in range(i):
    for x in range(j):
        pa = 0
        for mov in range(5):
            if(x+dx[mov] > -1 and x+dx[mov]<j and y+dy[mov] > -1 and y+dy[mov]<i):
                if(mapa[y+dy[mov]][x+dx[mov]] == "X"):
                    pa+=1
        
        if(pa == 0):
            f += 1
print(f)
