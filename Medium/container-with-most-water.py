#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/
# Language: Python3
# Date: 2025-11-21


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            currArea = min(height[left] , height[right]) * (right - left)
            area = max(area, currArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1  

        return area

        

        

