class Solution:
    def findIntegers(self, n: int) -> int:
        dpZero, dpOne, dp = [0] * 32, [0] * 32, [0] * 32
        dpZero[0] = dp[0] = 1
        for i in range(1, 32):
            dpOne[i] = dpZero[i-1]
            dpZero[i] = dpZero[i-1] + dpOne[i-1]
            dp[i] = dpZero[i] + dpOne[i]
            
        res, oldBit = 0, -1
        for j in range(30, -1, -1):
            bit = (n >> j) & 1
            if bit == 1:
                res += dp[j]
                if oldBit == 1: return res 
            oldBit = bit
            
        return res + 1  
