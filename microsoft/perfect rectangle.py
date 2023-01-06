class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        c = lambda: (b-y) * (a-x)
        
        for x, y, a, b in rectangles:
            area += c()
            corners ^= {(x,y), (x,b), (a,y), (a,b)}

        if len(corners) != 4: return False
        x, y = min(corners, key=lambda x: x[0] + x[1])
        a, b = max(corners, key=lambda x: x[0] + x[1])
        return c() == area
