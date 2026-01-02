#
# Problem: 695. Max Area of Island
# Difficulty: Medium
# Link: https://leetcode.com/problems/max-area-of-island/submissions/1872147953/
# Language: python3
# Date: 2026-01-02


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        change = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def bfs(i,j):
            grid[i][j] = 0
            queue = deque([(i,j)])
            area = 0
            while queue:
                x, y = queue.popleft()
                area += 1
                for dx, dy in change:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
            return area

        maxA = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxA = max(maxA, bfs(i, j))
        print(grid)
        return maxA
        
