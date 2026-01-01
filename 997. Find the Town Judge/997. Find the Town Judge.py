#
# Problem: 997. Find the Town Judge
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-town-judge/submissions/1871069343/
# Language: python3
# Date: 2026-01-01


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (n + 1)

        for (a,b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1

        for i in range(1, len(Trusted)):
            if Trusted[i] == n-1:
                return i
        return -1
