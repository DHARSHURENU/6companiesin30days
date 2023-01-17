class Solution:
    def magicalString(self, n: int) -> int:
        s="1"
        i,j=0,0
        while j<n:
            if s[j]=="1":
                s+="2"if s[-1]=="1"else"1"
                i+=1
            else:
                s+="12"if s[-1]=="1"else"21"
                i+=2
            j+=1
        return s[:n].count("1")
