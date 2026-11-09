class Solution(object):
    def findMismatchedSegments(self, s1, s2):
        f = []
        va1 = ""
        va2 = ""

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                va1 += s1[i]
                va2 += s2[i]
            else:
                if len(va1) > 0:
                    f.append([va1, va2])
                    va1 = ""
                    va2 = ""

        if len(va1) > 0:
            f.append([va1, va2])

        return f