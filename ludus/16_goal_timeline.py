n = int(input())
prim = []
segu = []
for i in range(n):
    tie, ape = input().split()
    if(int(tie[0:2]) < 46):
        try:
            prim.append((int(tie[0:2])+int(tie[3:]), ape))
        except:
            prim.append((int(tie[0:2]),ape))
    else:
        try:
            segu.append((int(tie[0:2])+int(tie[3:]),ape))
        except:
            segu.append((int(tie[0:2]),ape))
prim = sorted(prim)
segu = sorted(segu)
for t,ap  in prim:
    if t>45:
        a = str(t-45)
        t = str(45)
        print(t+"+"+a+" "+ap)
    else:
        t = str(t)
        print(t+" "+ap)

for t,ap  in segu:
    if t>90:
        a = str(t-90)
        t = str(90)
        print(t+"+"+a+" "+ap)
    else:
        t = str(t)
        print(t+" "+ap)