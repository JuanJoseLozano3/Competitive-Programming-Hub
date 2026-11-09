class Solution:
    def countValidSubstrings(self, s: str) -> int:
        t = len(s)
        posA = [-1]*t
        posB = [-1]*t
        posC = [-1]*t

        siA = siB = siC = -1

        def rec(i):
            nonlocal siA, siB, siC

            if i < 0:
                return

            if s[i] == "a":
                siA = i
            if s[i] == "b":
                siB = i
            if s[i] == "c":
                siC = i

            posA[i] = siA
            posB[i] = siB
            posC[i] = siC

            rec(i-1)

        rec(t-1)

        p = 0

        for i in range(t):
            p1 = posA[i]

            if p1 != -1:
                p2 = posB[p1]

                if p2 != -1:
                    p3 = posC[p2]

                    if p3 != -1:
                        p += t-p3

        return (t*(t+1))//2-p