class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calSteps(n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps
        c = 1
        k -= 1
        while k:
            steps = calSteps(c, c + 1)
            if steps <= k:
                c += 1
                k -= steps
            else:
                c*= 10
                k -= 1
        return c
