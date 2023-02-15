class Fenwick: 
    def __init__(self, n: int):
        self.nums = [0]*(n+1)

    def update(self, k: int, x: int) -> None: 
        k += 1
        while k < len(self.nums): 
            self.nums[k] += x
            k += k & -k 

    def query(self, k: int) -> int: 
        k += 1
        ans = 0
        while k:
            ans += self.nums[k]
            k -= k & -k
        return ans

    
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        mp = {x : i for i, x in enumerate(nums1)}
        fw = Fenwick(n)
        ans = 0 
        for i, x in enumerate(nums2):
            x = mp[x]
            left = fw.query(x)
            right = (n-1-x) - (fw.query(n-1)-left)
            ans += left * right
            fw.update(x, 1)
        return ans
