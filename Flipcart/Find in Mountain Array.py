# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def getpeak(self,A):
        l,r=0,A.length()-1
        while l<r:
            mid=(l+r)//2
            t=A.get(mid)
            T=A.get(mid-1)
            if T<t:
                l=mid+1
            else:
                r=mid
        return l-1
    def leftbs(self,l,r,A,k):
        while l<r:
            mid=(l+r)//2
            t=A.get(mid)
            if t<k:
                l=mid+1
            else:
                r=mid
        return l
    def rightbs(self,l,r,A,k):
        while l<r:
            mid=(l+r)//2
            t=A.get(mid)
            if t>k:
                l=mid+1
            else:
                r=mid
        return l
    def findInMountainArray(self, target: int, A: 'MountainArray') -> int:
        peak=self.getpeak(A)
        left=self.leftbs(0,peak,A,target)
        right=self.rightbs(peak,A.length()-1,A,target)
        if A.get(left)==target:
            return left
        if A.get(right)==target:
            return right
        return -1
