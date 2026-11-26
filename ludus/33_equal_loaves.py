n = int(input())
pan = list(map(int,input().split()))
mi = min(pan)
ch = 0
cu = 0
for i in pan:
    if(i!=mi):
       ch+=i-mi
    else:
        cu += 1
print(ch,cu)



















