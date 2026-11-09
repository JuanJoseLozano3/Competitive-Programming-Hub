class Solution:
    def reverseVowels(self, s: str) -> str:
        p = []
        h = set(["a","e","i","o","u", "A","E","I","O","U"])
        for i in range(len(s)):
            if s[i] in h:
                p.append(i)
        f = ""
        for i in range(len(s)):
            if(s[i] in h):
                f+=s[p[-1]]
                p.pop()
            else:
                f+=s[i]
        return f
        