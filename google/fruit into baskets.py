class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt=defaultdict(int)
        i,j=0,0
        for j in range(len(fruits)):
            cnt[fruits[j]]+=1
            if len(cnt)>2:
                cnt[fruits[i]]-=1
                if cnt[fruits[i]]==0:
                    del cnt[fruits[i]]
                i+=1
        return j-i+1
