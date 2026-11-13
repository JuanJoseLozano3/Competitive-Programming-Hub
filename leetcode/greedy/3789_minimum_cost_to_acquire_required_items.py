class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        t = 0
        if(cost1+cost2 > costBoth):
            men = min(need1,need2)
            t += men*costBoth
            need1-=men
            need2-=men
        if(cost1>costBoth):
            t += need1*costBoth
            need1 = 0
        else:
            t += need1*cost1
            need1 = 0
        if(cost2>costBoth):
            t += need2*costBoth
            need2 = 0
        else:
            t += need2*cost2
            need2 = 0
        return t