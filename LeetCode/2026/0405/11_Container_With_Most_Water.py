class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_container = 0

        while left < right:
            current_container = (right - left) * min(height[left], height[right])

            if(current_container > max_container):
                max_container = current_container

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_container
        