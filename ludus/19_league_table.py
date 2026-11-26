e, p = map(int,input().split())
tabla = []
nom = {}
for i in range(e):
    equipo = input()
    tabla.append([0,0,0,equipo])
    nom[equipo] = i

for _ in range(p):
    e1, g1, g2, e2 = input().split()
    g1 = int(g1)
    g2 = int(g2)
    if(g1>g2):
        tabla[nom[e1]][0] += 3
        tabla[nom[e1]][1] += g1-g2
        tabla[nom[e1]][2] += g1
        tabla[nom[e2]][1] += g2-g1
        tabla[nom[e2]][2] += g2
    elif(g1==g2):
        tabla[nom[e1]][0] += 1
        tabla[nom[e1]][2] += g1
        tabla[nom[e2]][0] += 1
        tabla[nom[e2]][2] += g2
    else:
        tabla[nom[e1]][1] += g1-g2
        tabla[nom[e1]][2] += g1
        tabla[nom[e2]][0] += 3
        tabla[nom[e2]][1] += g2-g1
        tabla[nom[e2]][2] += g2

f = tabla
f.sort(key=lambda x: x[3])
f.sort(key=lambda x: x[2], reverse=True)
f.sort(key=lambda x: x[1], reverse=True)
f.sort(key=lambda x: x[0], reverse=True)

for i in f:
    print(i[3]+" "+str(i[0])+" "+str(i[1])+" "+str(i[2]))