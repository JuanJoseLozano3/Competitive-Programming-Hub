class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        def rec(lista, actual):
            if not lista:
                res.append(actual[:])
                return
            a = lista[0]
            for i in range(1, len(lista)):
                b = lista[i]
                par = [a,b]
                if par in com:
                    continue
                actual.append(par)

                restantes = lista[1:i] + lista[i+1:]
                rec(restantes, actual)

                actual.pop()


        d = [0]*n
        com = []
        for i in edges:
            d[i[0]-1] += 1
            d[i[1]-1] += 1
            com.append(i)
            com.append([i[1],i[0]])
        c = []
        h = []
        p = 0
        t = 0
        for i in range(n):
            if(d[i]%2!=0):
                p+=1
                c.append(i+1)
            if(d[i]%2==0 and d[i]<n-1):
                h.append(i+1)
            if(d[i]==n-1):
                t+=1
        print(d)
        print(c)
        if(t>0 and n%2==0):
            return False
        else:
            if(p>4):
                return False
            res = []
            rec(c, [])
            print(res)
            if(len(res)>0):
                return True
            fin = n-t
            if(fin>p):
                if(p==2):
                    k = False
                    for i in h:
                        if([i,c[0]] in com):
                            continue
                        if([i,c[1]] in com):
                            continue
                        k = True
                        break
                    return k
                else:
                    return False
            else:
                return False
        
