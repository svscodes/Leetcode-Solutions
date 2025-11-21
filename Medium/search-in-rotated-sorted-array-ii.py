#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Language: Python3
# Date: 2025-11-21


                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         left, right = 0, len(nums)-1

#         while left <= right:
#             mid = (left + right)//2

#             if nums[mid] == target:
#                 return True

            else:
                    low = mid + 1
                    high = mid - 1
                else:
                if nums[low] <= target <= nums[mid]:
            
            if nums[low] <= nums[mid]:
                continue
                low += 1
         
            if nums[low] == nums[mid]:
                return True
            if nums[mid] == target:
            mid = (low + high) // 2
        while low <= high:

        low, high = 0, len(nums) - 1
    def search(self, nums: List[int], target: int) -> bool:
class Solution:
