n = int(input())
w, d, l, p = 0,0,0,0
for i in range(n):
    yo, el = map(int,input().split())
    if(yo>el):
        w+=1
        p+=3
    elif(yo==el):
        d+=1
        p+=1
    else:
        l += 1
print(w,d,l,p)