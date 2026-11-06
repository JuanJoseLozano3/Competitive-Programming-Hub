from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        f = queries.copy()
        dic = defaultdict(set)
        for i in logs:
            dic[i[1]].add(i[0])

        tiempos = sorted(dic.keys())

        dic2 = defaultdict(int)
        serv = defaultdict(int)
        queries = sorted(queries)
        finant = 0
        iniant = 0

        for i in range(len(queries)):
            if queries[i] in dic2:
                continue

            ini = queries[i] - x
            fin = queries[i]

            if ini > finant:
                suma = 0
                serv = defaultdict(int)

                for j in tiempos[bisect_left(tiempos, ini):bisect_right(tiempos, fin)]:
                    for k in dic[j]:
                        if serv[k] == 0:
                            suma += 1
                        serv[k] += 1

                iniant = ini
                finant = fin
                dic2[fin] = suma

            else:
                suma = dic2[queries[i-1]]

                for j in reversed(tiempos[bisect_left(tiempos, iniant):bisect_left(tiempos, ini)]):
                    for h in dic[j]:
                        serv[h] -= 1
                        if serv[h] == 0:
                            suma -= 1

                for j in tiempos[bisect_right(tiempos, finant):bisect_right(tiempos, fin)]:
                    for h in dic[j]:
                        serv[h] += 1
                        if serv[h] == 1:
                            suma += 1

                dic2[fin] = suma
                finant = fin
                iniant = ini

        final = []
        for i in f:
            final.append(n - dic2[i])

        return final
