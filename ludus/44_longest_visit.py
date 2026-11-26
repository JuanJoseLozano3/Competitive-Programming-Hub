n = int(input())
ma = -1
gan = 0
for i in range(n):
    ent, sal = input().split()
    h1 = int(ent[0:2])
    m1 = int(ent[3:])
    h2 = int(sal[0:2])
    m2 = int(sal[3:])
    if(h1<h2):
        val = (h2-h1)*60+(m2-m1)
        if(val > ma):
            ga = i+1
            ma = val
    elif(h1>h2):
        val = (24-(h1-h2))*60+(m1-m2)
        if(val > ma):
            ga = i+1
            ma = val
    elif(h1==h2 and m1<m2):
        val = (m2-m1)
        if(val > ma):
            ga = i+1
            ma = val
    elif(h1==h2 and m1>m2):
        val = (24)*60+(m1-m2)
        if(val > ma):
            ga = i+1
            ma = val
    else:
        val = 0
        if(val > ma):
            ga = i+1
            ma = val

print(ga, ma)

