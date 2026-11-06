n = int(input())
te = input()

tam = len(te)
tex = []
for i in range(tam):
    tex.append(i)

flag = tam%2 != 0

c = tuple(tex)
tipos = {}
vis = set()
i = 0
while True:
    if c in vis:
        break
    tipos[i] = c
    vis.add(c)
    c = []
    for j in range(tam//2):
        c.append(tex[j])
        c.append(tex[tam-1-j])
    if(flag):
        c.append(tex[tam//2])
    tex = c.copy()
    c = tuple(tex)
    i+= 1
    
n = n%(len(tipos))
if(n==0):
    res = ""
    for i in tipos[0]:
        res += te[i]
    print(res)
else:
    res = ""
    for j in tipos[i-n]:
        res += te[j]
    print(res)
