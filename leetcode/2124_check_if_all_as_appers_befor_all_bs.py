class Solution:
    def checkString(self, s: str) -> bool:
        f = True
        for i in s:
            if i == "b":
                f = False
            elif i == "a" and f:
                continue
            else:
                return False
        return True