from collections import defaultdict
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        final = float("inf")

        def dp(pos,cost):
            nonlocal final
            if(pos in memo):
                return cost + memo[pos]
            if(pos==n):
                return cost
            if(pos<n):
                p = cost + costs[pos]+((pos+1)-pos)**2
                p = dp(pos+1,p)
                final = min(final,p)
            if(pos<n-1):
                p = cost + costs[pos+1]+((pos+2)-pos)**2
                p = dp(pos+2,p)
                final = min(final,p)
            if(pos<n-2):
                p = cost + costs[pos+2]+((pos+3)-pos)**2
                p = dp(pos+3,p)
                final = min(final,p)
            
            memo[pos] = final - cost
            return final
        
        memo = defaultdict(int)
        final = dp(0,0)
        return final