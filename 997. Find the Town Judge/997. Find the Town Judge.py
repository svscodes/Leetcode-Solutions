#
# Problem: 997. Find the Town Judge
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-town-judge/submissions/1871064295/
# Language: python3
# Date: 2026-01-01


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        if len(trust) < n-1:
            return -1
        else:
            lst = {}
            for i in range(len(trust)):
                if trust[i][1] in lst:
                    lst[trust[i][1]].append(trust[i][0])
                else:
                    lst[trust[i][1]] = []
                    lst[trust[i][1]].append(trust[i][0])
            print(lst)
            for i in lst:
                if len(lst[i]) == n - 1:
                    all_flat_values = [item for sublist in lst.values() for item in sublist]
                    if i not in all_flat_values:
                        return i
            return -1

