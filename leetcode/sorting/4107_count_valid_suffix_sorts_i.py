from collections import defaultdict

class Solution(object):
    def countSuffix(self, nums, target):
        t = len(nums)
        pos = -1
        for i in range(t-2, -1, -1):
            if target[i] < target[i+1]:
                pos = i
                break

        for i in range(pos+1):
            if nums[i] != target[i]:
                return 0

        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        for i in range(pos+1, t):
            dic1[nums[i]] += 1
            dic2[target[i]] += 1

        if dic1 != dic2:
            return 0

        c = 0
        for i in range(pos+1, t):
            c += 1
            if nums[i] != target[i]:
                return c

        return c
        