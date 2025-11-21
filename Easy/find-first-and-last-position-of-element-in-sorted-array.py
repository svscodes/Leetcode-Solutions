#
# Problem: 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Language: Python3
# Date: 2025-11-21


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left = 0
        # right = len(nums)-1
        # start = -1
        # end = -1

        # def first(self,nums,target){
        #     idx = -1
        #     low,high = 0,len(nums)-1

        #     while low<=high:
        #         mid = lo

        # }

        # def last(self,nums,target){

        # }

        # while left < right:
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         if nums[mid-1] != target:
        #             start = mid
        #         else:
        #             start = self.first(nums,target)

        
        #         if nums[mid+1] != target:
        #             end = mid
        #         else:
        #             end = self.last(nums,target)


        #     elif nums[mid] < target:
        #         left = mid+1
        #     else:
        #         right = mid-1

                 
        # return [start,end]
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]


        
