class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        d = 0
        for i in range(len(points)):
            dt= dict()
            for j in range(len(points)):
                if j != i:
                    hd = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                    d += dt.get(hd, 0)
                    dt[hd] = dt.get(hd , 0) + 1
        return d * 2
