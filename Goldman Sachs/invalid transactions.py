class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res=[]
        h=collections.defaultdict(list)
        for d in transactions:
            n,t,a,c=d.split(',')
            t,a=int(t),int(a)
            h[n].append({'t':t,'c':c})
        for d in transactions:
            n,t,a,c=d.split(',')
            t,a=int(t),int(a)
            if a>1000:
                res.append(d)
            elif n in h:
                for sameName in h[n]:
                    if abs(sameName['t']-t)<=60 and sameName['c']!=c:
                        res.append(d)
                        break
        return res
                        
