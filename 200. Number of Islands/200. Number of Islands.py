#
# Problem: 200. Number of Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-islands/submissions/1872128606/
# Language: python3
# Date: 2026-01-02


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS

        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    cnt += 1
                
        return cnt


