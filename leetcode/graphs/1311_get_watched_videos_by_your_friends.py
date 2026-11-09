from collections import deque
from collections import defaultdict
class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        
        visitados = set()
        cola = deque()
        cola.append(id)
        visitados.add(id)
        
        va = defaultdict(int)
        va[id] = 0
        while cola:
            amigo = cola.popleft()
            for ami in friends[amigo]:
                if ami not in visitados:
                    va[ami] = va[amigo]+1
                    visitados.add(ami)
                    cola.append(ami)
        
        k = defaultdict(int)
        for c,v in va.items():
            if(v == level):
                for i in watchedVideos[c]:
                    k[i] += 1

        k = dict(sorted(k.items(), key=lambda x: (x[1], x[0])))

        l = []
        for c,v in k.items():
            l.append(c)
        return l