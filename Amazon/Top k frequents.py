class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dc=defaultdict(lambda:0)
        for a in words:
            dc[a]+=1
        arr=[]
        for a in dc:
            arr.append([dc[a],a])
        arr.sort(key=lambda x:(1/x[0],x[1]))
        ans=[]
        for i in range(k):
            ans.append(arr[i][1])
        return ans
