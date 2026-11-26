s = input()
t = len(s)
if(t%2==0):
   re = 0
   for i in range(t//2):
      if(s[i]!=s[t-1-i]):
        re += 1
else:
    re = 0
    for i in range(t//2):
        if(s[i]!=s[t-1-i]):
            re+=1
print(re)

















