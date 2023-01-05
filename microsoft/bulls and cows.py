class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c1 = Counter(secret)
        c2 = Counter(guess)
        c = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                c += 1
                c1[secret[i]] -= 1
                c2[secret[i]] -= 1
        n = 0
        for k in c2.keys():
            if k in c1:
                n += min(c1[k], c2[k])
        return str(c)+'A'+str(n)+'B'
