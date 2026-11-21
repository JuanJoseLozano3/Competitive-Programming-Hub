class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        area = 0
        t = len(points)
        for i in range(t):
            for j in range(i+1,t):
                for k in range(j+1,t):
                    cal = (points[i][0]*(points[j][1]-points[k][1])+points[j][0]*(points[k][1]-points[i][1])+points[k][0]*(points[i][1]-points[j][1]))/2
                    if(abs(cal)>area):
                        area = abs(cal)
        return area