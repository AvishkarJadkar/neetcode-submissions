class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarysearch(nums, target, True)
        right = self.binarysearch(nums, target, False)
        return [left, right]
    

    def binarysearch(self, nums, target, leftBias):
        left = 0
        right = len(nums) - 1
        i = -1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                i = middle

                if leftBias:
                    right = middle - 1

                else:
                    left = middle + 1

            elif nums[middle] < target:
                left = middle + 1

            else:
                right = middle - 1
        return i
        