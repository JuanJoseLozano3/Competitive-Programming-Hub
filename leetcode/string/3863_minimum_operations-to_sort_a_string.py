class Solution:
    def minOperations(self, s: str) -> int:
        tam = len(s)
        a = sorted(s)
        if (list(s) == a):
            return 0
        if tam < 3:
            return -1
        elif (s[0] == a[0] or s[-1] == a[-1]):
            return 1
        elif (a[0] in s[1:-1] or a[-1] in s[1:-1]):
            return 2
        else:
            return 3