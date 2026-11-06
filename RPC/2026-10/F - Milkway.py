from collections import defaultdict
from bisect import bisect_left

n, q = map(int,input().split())
nums = list(map(int,input().split()))
queries = []
for i in range(q):
    queries.append(list(map(int,input().split())))

rup = [0]
prob = []
c = 0
for i in range(1,len(nums)):
    if(nums[i]<nums[i-1]):
        prob.append([i,i+1])
        c+= 1
    rup.append(c)

for t in queries:
    print("NO") if rup[t[0]-1]!=rup[t[1]-1] else print("YES")



