class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        t = len(customers)
        prefix = [0]*t
        cam = 0
        van = 0
        for i in range(t):
            if(grumpy[i] == 0):
                cam += customers[i]
            if(grumpy[i] == 1):
                van += customers[i] 
            prefix[i] = van
        m = prefix[minutes-1]
        for i in range(minutes,t):
            m = max(m, prefix[i]-prefix[i-minutes])
        return cam + m 
        