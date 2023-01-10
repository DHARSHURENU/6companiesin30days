class Solution:
    def trailingZeroes(self, n: int) -> int:
        pdt=1
        cnt=0
        while n>1:
            cnt += n//5
            n//=5
        return cnt
        
