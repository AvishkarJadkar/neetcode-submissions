class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1

            else:
                count = 0

            maximum_count = max(maximum_count, count)
        
        return maximum_count