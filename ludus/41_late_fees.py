n,d,f = map(int,input().split())
dic = {"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31, "09":30,"10":31,"11":30,"12":31}
di2 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
v = 0
for i in range(n):
    sal, vue = input().split()
    sumad = 0
    if(int(vue[3:]) > int(sal[3:])):
        sumad += dic[sal[3:]] - int(sal[0:2])
        for i in range(int(sal[3:])+1, int(vue[3:])):
            sumad += di2[i]
        sumad += int(vue[0:2])
    elif(int(vue[3:]) == int(sal[3:]) and int(vue[0:2]) >= int(sal[0:2])):
        sumad += int(vue[0:2]) - int(sal[0:2])
    else:
        sumad += dic[sal[3:]] - int(sal[0:2])
        i = int(sal[3:])+1
        while i != int(vue[3:]):
            if(i==13):
                i=1
            sumad += di2[i]
            i+=1
        sumad += int(vue[0:2])
    sumad = max(0,sumad-d)
    v+= sumad*f
print(v)
    
