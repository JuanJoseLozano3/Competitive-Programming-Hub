class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        
        arr = sorted(arr)
        diff = abs(arr[0]-arr[1])
        for i in range(1,len(arr)):
            if(abs(arr[i]-arr[i-1])!=diff):
                return False
        return True

        """
        :type arr: List[int]
        :rtype: bool
        """
        