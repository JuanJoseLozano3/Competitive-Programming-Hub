class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        prom = 0
        for i in range(k):
            prom += arr[i]
        prom/=k
        c = 0
        if(prom >= threshold):
            c+=1
        for i in range(k,len(arr)):
            prom += arr[i]/k
            prom -= arr[i-k]/k
            if(prom >= threshold):
                c+=1
        return c