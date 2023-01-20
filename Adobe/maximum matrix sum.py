class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_tot = neg = 0
        h= math.inf
        for row in matrix:
            for num in row:
                abs_tot += abs(num)
                if num < 0:
                    neg += 1
                h = min(h, abs(num))
        return abs_tot if neg % 2 == 0 else abs_tot - 2 * h
                
                
        
