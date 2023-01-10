class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if(p1==p2 or p1==p3 or p1==p4 or p2==p3 or p2==p4 or p3==p4):
            return False
        s=set()
        s.add(math.dist(p1,p2))
        s.add(math.dist(p1,p3))
        s.add(math.dist(p1,p4))
        s.add(math.dist(p2,p3))
        s.add(math.dist(p2,p4))
        s.add(math.dist(p3,p4))
        if len(s)==2:
            return True
        else:
            return False
