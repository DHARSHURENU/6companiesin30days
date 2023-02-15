class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums)
    def bubble_sort(self, nums):
        for i in range(len(nums)):
            swap = False
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if swap == False:
                break
        return nums
    def insertion_sort(self, nums):
        for step in range(1, len(nums)):
            key = nums[step]
            j = step - 1
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums
    def selection_sort(self, nums):
        for i in range(len(nums)):
            n = len(nums)
            min_index = i
            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
    def merge_sort(self, nums):
        def merge_sort_helper(nums, left, right, temp):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort_helper(nums, left, mid, temp)
            merge_sort_helper(nums, mid+1, right, temp)
            merge(nums, left, mid, right, temp)
        def merge(nums, left, mid, right, temp):
            i, j = left, mid + 1
            k = 0
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1
            for i in range(k):
                nums[left + i] = temp[i]       
        temp = [0 for _ in range(len(nums))]
        merge_sort_helper(nums, 0, len(nums)-1, temp)
        return nums
    def quick_sort(self, nums):
        def quick_sort_helper(nums, left, right):
            if left >= right:
                return 
            i, j = left, right
            pivot = nums[random.randint(left, right)]
            while i <= j:
                while i <= j and nums[i] < pivot:
                    i += 1
                while i <= j and nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            quick_sort_helper(nums, left, j)
            quick_sort_helper(nums, i, right)
        quick_sort_helper(nums, 0, len(nums) - 1)
        return nums
