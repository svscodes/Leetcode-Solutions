#
# Problem: 994. Rotting Oranges
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotting-oranges/description/
# Language: python3
# Date: 2026-01-13


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi source BFS with count of total solns


        row, col = len(grid), len(grid[0]) 
        mins, fo = 0, 0
        nxt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fo += 1

        while q and fo!= 0:

            for i in range(len(q)):
                x,y = q.popleft()
                for dx, dy in nxt:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < row and 0<= ny < col and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        fo -= 1
            mins += 1

        return mins if fo == 0 else -1
