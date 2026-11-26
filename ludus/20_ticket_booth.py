n = int(input())
for i in range(n):
    v, p = map(int,input().split())
    mon = 0
    c = p-v
    mon += c//200
    c %= 200
    mon += c//100
    c %= 100
    mon += c//50
    c %= 50
    mon += c//20
    c %= 20
    mon += c//10
    c %= 10
    mon += c//5
    c %= 5
    mon += c//2
    c %= 2
    mon += c//1
    c %= 1
    print(mon)