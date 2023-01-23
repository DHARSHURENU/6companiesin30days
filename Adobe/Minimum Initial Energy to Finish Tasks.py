class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        res = c = 0
        for cost, min in tasks:
            if min > c:
                res += (min - c)
                c = min
            c-= cost
        return res
