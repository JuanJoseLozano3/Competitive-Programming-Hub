class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        pro = []
        for i in range(1, k + 1):
            pro.append(i)

        final = []
        va = k - 2
        cuan = 0
        c = pro.copy()
        final.append(c)
        f = set()
        f.add(tuple(c))

        while pro[0] < n - k + 1:
            c = pro.copy()

            for j in range(c[-1], n):
                p = c.copy()
                p[-1] += 1
                c = p.copy()
                if tuple(c) not in f:
                    final.append(c)
                    f.add(tuple(c))

            if pro[va] < n - cuan:
                pro[va] += 1
                val = pro[va]
                j = va + 1
                c = 1

                while j < k:
                    pro[j] = val + c
                    c += 1
                    j += 1

                if pro[-1] <= n:
                    p = pro.copy()
                    if tuple(p) not in f:
                        final.append(p)
                        f.add(tuple(p))

                va = k - 2
                cuan = 0
            else:
                cuan += 1
                va -= 1

                if va < 0:
                    break

        return final