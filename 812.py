# 812. Largest Triangle Area
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # I was going to use heron's formula, but for this problem I learned about the shoelace formula which is much easier to implement.
        # we want 3 nested loops that start at i+1 and j+1 to prevent duplicate triangles.
        # perhaps there could be small checks to skip triangles that are not possible
        # for example if they are on the same line (colinear)
        maxArea=0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    area=0.5*abs(points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1] - (points[i][1] * points[j][0] + points[j][1] * points[k][0] + points[k][1] * points[i][0]))
                    if area>maxArea:
                        maxArea=area
        return maxArea