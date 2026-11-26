h,m,t = map(int,input().split())

suma = t//60
h+= suma

t%=60
m += t
if(m>59):
    m%=60
    h+=1
h%=24

h = str(h)
m = str(m)
if(len(h)<2 and len(m)<2):
    print("0"+h+":0"+m)
elif(len(h)<2):
    print("0"+h+":"+m)
elif(len(m)<2):
    print(h+":0"+m)
else:
    print(h+":"+m)
















