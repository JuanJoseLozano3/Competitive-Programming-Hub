from collections import defaultdict
n = int(input())
for i in range(n):
    p, a, b = map(int,input().split())
    cond1 = True if a*b==p else False
    cond2 = True if len(str(a)) == len(str(p))/2 and len(str(b))==len(str(p))/2 else False
    cond3 = True if a%10!=0 or b%10!=0 else False
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    k1 = str(a)+str(b)
    k2 = str(p)
    if(len(k1)!=len(k2)):
        cond4=False
    else:
        for q in range(len(k1)):
            dic1[k1[q]] += 1
            dic2[k2[q]] += 1
        cond4 = True if dic1==dic2 else False
    print("YES") if (cond1==cond2==cond3==cond4==True) else print("NO")

