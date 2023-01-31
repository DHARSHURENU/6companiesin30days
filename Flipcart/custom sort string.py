class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict={}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        res=''
        for x in order:
            if x in s:
                res+=x*dict[x]
        for y in s:
            if y not in res:
                res+=y*dict[y]
        return res
        
