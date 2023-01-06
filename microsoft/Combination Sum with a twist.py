class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(num, k, n, tmp):
            if k == 0:
                if n == 0:
                    res.append(tmp[:])
                return
            for i in range(num, 10):
                if i > n:
                    return
                tmp.append(i)
                dfs(i + 1, k - 1, n - i, tmp)
                tmp.pop()

        res = []
        dfs(1, k, n, [])
        return res
       
