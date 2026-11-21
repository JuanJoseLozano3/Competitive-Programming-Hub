class Solution(object):
    def pivotInteger(self, n):
        if n== 1:
            return 1
        li = []
        for i in range(n):
            li.append(((i+1)*(i+2))/2)

        for i in range(n-2,-1,-1):
            #print(li[i],(li[-1]-li[i-1]))
            if(li[i]==(li[-1]-li[i-1])):
               return i+1
  
        return -1
            
        """
        :type n: int
        :rtype: int
        """
        