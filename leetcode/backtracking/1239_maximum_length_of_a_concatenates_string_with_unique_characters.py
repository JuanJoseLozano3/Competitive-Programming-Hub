class Solution:
    def maxLength(self, arr: list[str]) -> int:
        li = []
        t = len(arr)
        for i in range(t):
            k = set()
            for j in arr[i]:
                k.add(j)
            if(len(k)==len(arr[i])):
                li.append(k)

        concat = [set()]
        for u in li:
            for c in concat:
                if not c & u:
                    concat.append(c | u)
        ma = 0
        for i in concat:
            ma = max(ma,len(i))
        return ma