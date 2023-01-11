class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for e in nums:
            count[e] += 1
        F = defaultdict(int)
        for e in nums:
            if count[e] == 0:
                continue
            count[e] -= 1
            if F[e - 1] > 0:
                F[e - 1] -= 1
                F[e] += 1
            elif count[e + 1] > 0 and count[e + 2] > 0:
                F[e + 2] += 1
                count[e + 1] -= 1
                count[e + 2] -= 1
            else:
                return False
        return True
                
                
                    
        
