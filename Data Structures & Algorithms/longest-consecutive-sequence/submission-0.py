class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            current_num = num
            current_length = 1

            while current_num + 1 in nums:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

        return longest