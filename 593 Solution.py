import math
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]

        def dist2(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2

        d = []

        for i, a in enumerate(points):
            for b in points[i + 1:]:
                d.append(dist2(a, b))

        d.sort()

        return (
        d[0] > 0 and
        d[0] == d[1] == d[2] == d[3] and 
        d[4] == d[5] and
        d[4] == 2 * d[0]   
        )        


