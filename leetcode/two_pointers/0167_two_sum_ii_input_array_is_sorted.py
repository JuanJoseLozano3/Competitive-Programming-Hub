class Solution:
    def twoSum(self, numbers: list[int], k: int) -> list[int]:
        ini = 0
        fin = len(numbers)-1
        while True:
            if(numbers[ini]+numbers[fin]==k):
                return [ini+1,fin+1]
            elif(numbers[ini]+numbers[fin]>k):
                fin -= 1
            else:
                ini += 1
