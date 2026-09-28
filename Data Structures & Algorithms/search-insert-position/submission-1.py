class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[middle] == target:
                return middle

            elif nums[middle] < target:
                left = middle + 1

            else:
                right = middle - 1

        if nums[middle] < target:
            return middle + 1

        else:
            return middle