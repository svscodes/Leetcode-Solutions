#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/coin-change/submissions/1892392214/
# Language: python3
# Date: 2026-01-21


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
            print(a, dp[a])

        return dp[amount] if dp[amount] != amount + 1 else -1
