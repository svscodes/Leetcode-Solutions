#
# Problem: 78. Subsets
# Difficulty: Medium
# Link: https://leetcode.com/problems/subsets/
# Language: Python3
# Date: 2025-11-21


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
         
