class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            width = right - left

            if heights[left] < heights[right]:
                area = heights[left] * width
                left += 1

            else:
                area = heights[right] * width
                right -= 1

            max_area = max(area, max_area)

        return max_area