import math
n = int(input())
for i in range(n):
    s,k,a = map(int,input().split())
    if(a<=s):
        print(s-a)
    else:
        p = math.ceil((a-s)/k)
        num = s+(p*k)
        print(num-a)
