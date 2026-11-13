n = int(input())
li = list(map(int,input().split()))

k = 1
b = 1
for i in range(1,n):
    if(li[i]>li[0]):
        k+=1
    else:
        break
if(k == n):
    print("infinity")
else:
    print(k)
