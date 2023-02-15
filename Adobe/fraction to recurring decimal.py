class Solution:
    def fractionToDecimal(self, nu: int, de: int) -> str:
        cf=""
        if(nu*de<0):
            cf="-"
        nu=abs(nu)
        de=abs(de)
        st1=nu//de
        re=abs(nu%de)
        st1=str(st1)
        st2=""
        i=0
        dc={}
        while(re>0):
            if(re<de):
                re*=10
            if((re,de) in dc):
                st2=st2[:dc[(re,de)]]+"("+st2[dc[(re,de)]:]+")"
                break
            dc[(re,de)]=i
            i+=1
            st2+=str(re//de)
            re=re%de
        if(st2==""):
            return cf+st1
        return(cf+st1+"."+st2)
