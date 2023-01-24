class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        h=set()
        for i in range(k,len(s)+1):
            h.add(s[i-k:i])
            if len(h)==1<<k:
                break
        return len(h)==1<<k
