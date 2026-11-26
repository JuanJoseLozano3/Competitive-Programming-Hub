from collections import defaultdict

n = input()
m = input()

dic1 = defaultdict(int)
dic2 = defaultdict(int)

for i in n:
    dic1[i]+=1
for i in m:
    dic2[i]+=1

can = float("inf")
for cl,val in dic1.items():
    can = min(can,dic2[cl]//val)

print(can)