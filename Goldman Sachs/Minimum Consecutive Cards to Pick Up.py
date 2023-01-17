class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res=float('inf')
        seen={}
        for i, n in enumerate(cards):
            if n in seen:
                if i-seen[n]+1 < res:
                    res=i-seen[n]+1
            seen[n]=i
        if res==float('inf'):
            return -1
        return res
