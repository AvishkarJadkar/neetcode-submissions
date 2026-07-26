class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for n in nums:
            if n > 0:
                positive.append(n)

            else:
                negative.append(n)

        i = 0 
        while (2*i) < len(nums):
            nums[2*i] = positive[i]
            nums[2*i + 1] = negative[i]

            i += 1

        return nums