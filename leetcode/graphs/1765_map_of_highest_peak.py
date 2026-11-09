from collections import deque

class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m = 0
        agua = []
        matrix = []
        for i in range(len(isWater)):
            a = []
            for j in range(len(isWater[0])):
                if(isWater[i][j] == 1):
                    agua.append((i,j))
                a.append(0)
            matrix.append(a)
        

        visitados = set()
        cola = deque()
        for i in agua:
            cola.append(i)
            visitados.add(i)
        
        while cola:
            i, j = cola.popleft()
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                ni = i + di
                nj = j + dj
                if(ni>=0 and nj>=0 and ni<len(isWater) and nj<len(isWater[0])):
                    if (ni,nj) not in visitados:
                        matrix[ni][nj] = matrix[i][j]+1
                        visitados.add((ni,nj))
                        cola.append((ni,nj))
        return matrix

