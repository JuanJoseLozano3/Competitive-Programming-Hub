i,j = map(int,input().split())
mapa = []

for ñ in range(i):
    k = input()
    c = []
    for m in k:
        c.append(m)
    mapa.append(c)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
mal = []
for y in range(i):
    po = []
    for x in range(j):
        chi = 0
        if(mapa[y][x]=="*"):
            po.append("*")
        else:
            for k in range(8):
                x1 = x+dx[k]
                y1 = y+dy[k]
                if(x1>-1 and x1<j and y1>-1 and y1<i):
                    if(mapa[y1][x1]=="*"):
                        chi += 1
            po.append(str(chi))
    mal.append(po)

for ka in range(i):
    print("".join(mal[ka]))