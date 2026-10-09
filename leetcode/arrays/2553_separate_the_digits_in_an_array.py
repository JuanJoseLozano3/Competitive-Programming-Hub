class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        f = []
        for i in nums:
            j = str(i)
            for k in j:
                f.append(int(k))
        return f
