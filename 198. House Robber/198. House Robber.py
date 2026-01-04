#
# Problem: 198. House Robber
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber/submissions/1874423632/
# Language: python3
# Date: 2026-01-04


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]
