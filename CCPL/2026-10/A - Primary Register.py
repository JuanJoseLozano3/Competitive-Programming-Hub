real = [2,3,5,7,11,13,17,19]
dada = list(map(int,input().split()))
n = 0
while True:
    try:
        n += 1
        dada[0] += 1
        for i in range(8):
            if(dada[i] == real[i]):
                dada[i] = 0
                dada[i+1] += 1
            else:
                break         
    except:
        break
print(n-1)

