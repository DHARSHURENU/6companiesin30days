class Solution:
    def closestPrimes(self, l: int, r: int) -> List[int]:
        prime = self.sieve(l,r)
        if len(prime) < 2 :
            return [-1,-1]
        diff = float(inf)
        res = [-1,-1]
        for i in range(len(prime)-1) :
            cdiff = prime[i+1] - prime[i]
            if cdiff < diff :
                res = [prime[i],prime[i+1]]
                diff = cdiff
        return res
    def sieve(self,min,n):  
        prime = [True]*(n+1)
        prime[0] = prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):   
            if prime[i] :  
                for j in range(i*i ,n+1 ,i):  
                    prime[j] = False
        return [i for i in range(min,len(prime)) if prime[i]]
    
