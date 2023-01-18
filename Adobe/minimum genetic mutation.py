class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q=[(startGene,0)]
        visit=set()
        bank=set(bank)
        while q:
            g,step=q.pop()
            if g==endGene:
                return step
            visit.add(g)
            for c in "ACGT":
                for i in range(8):
                    h=g[:i]+c+g[i+1:]
                    if h in bank and h not in visit:
                        q.append((h,step+1))
        return -1
