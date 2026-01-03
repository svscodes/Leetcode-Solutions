#
# Problem: 1137. N-th Tribonacci Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/n-th-tribonacci-number/submissions/1873261835/
# Language: python3
# Date: 2026-01-03


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]
