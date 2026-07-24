class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0

        for right in range (1, len(nums)):
            if nums[right] == nums[right - 1]:
                return True

        else:
            return False

    

        