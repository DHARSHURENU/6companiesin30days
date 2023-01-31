class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @functools.cache
        def count(i,j,k):
            if i<0 or i>=n or j<0 or j>=n: 
                return 0
            if k==0: 
                return 1
            res=0
            for x,y in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                res+=count(x+i,y+j,k-1)
            return res
        return count(row,column,k)/(8**k)
