class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n, SUM = len(nums), sum(nums)
        MAX = cur = sum(i*nums[i] for i in range(n))
        for i in range(1, n):
            cur += SUM - n * nums[n-i]
            MAX = max(MAX, cur)
        return MAX
