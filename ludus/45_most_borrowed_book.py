from collections import defaultdict
n = int(input())
ma = 0
dic = defaultdict(int)

for i in range(n):
    p = input()
    dic[p] += 1
    ma = max(ma,dic[p])

que = []
for cl,va in dic.items():
    if(va == ma):
        que.append(cl)

que = sorted(que)
print(que[0], dic[que[0]])