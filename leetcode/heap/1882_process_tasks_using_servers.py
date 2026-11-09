import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ser = []
        for i in range(len(servers)):
            heapq.heappush(ser, (servers[i], i))

        ans = []
        ocu = []
        tiempo = 0

        for i in range(len(tasks)):
            tiempo = max(tiempo, i)

            while ocu and ocu[0][0] <= tiempo:
                men = heapq.heappop(ocu)
                heapq.heappush(ser, (servers[men[1]], men[1]))

            if not ser:
                tiempo = ocu[0][0]

                while ocu and ocu[0][0] <= tiempo:
                    men = heapq.heappop(ocu)
                    heapq.heappush(ser, (servers[men[1]], men[1]))

            menor = heapq.heappop(ser)
            ans.append(menor[1])
            heapq.heappush(ocu, (tiempo + tasks[i], menor[1]))

        return ans