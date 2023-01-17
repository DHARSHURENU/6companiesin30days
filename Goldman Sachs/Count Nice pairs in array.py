class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        stat = {}
        dharshu = 10**9 + 7
        for i in range(n):
            diff = nums[i] - int(str(nums[i])[::-1])
            stat[diff] = stat.get(diff, 0) + 1
            if stat[diff] > 1:
                count += stat[diff] - 1
        return count % dharshu
