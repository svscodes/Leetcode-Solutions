#
# Problem: 7. Reverse Integer
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-integer/description/
# Language: python3
# Date: 2025-11-26


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            y = int(str(x)[::-1])
        else: 
            y = -int(str(x)[:0:-1])
        if y>= -2147483648 and y<=2147483647:
            return y 
        else:
            return 0 

