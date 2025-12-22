#
# Problem: 81. Search in Rotated Sorted Array II
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# Language: python3
# Date: 2025-12-22


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
         
            if nums[low] == nums[mid]:
                low += 1
                continue
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         left, right = 0, len(nums)-1

#         while left <= right:
#             mid = (left + right)//2

#             if nums[mid] == target:
#                 return True

#             if nums[left] == nums[mid]:
#                 left = left + 1
#                 continue

#             if nums[left] <= nums[mid]:
#                 if nums[left] <= target <= nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#             return False
    
