#
# Problem: 463. Island Perimeter
# Difficulty: Easy
# Link: https://leetcode.com/problems/island-perimeter/description/
# Language: python3
# Date: 2025-12-31


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        lists = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = deque([(i,j)])
                    grid[i][j] = 2
                    while queue:
                        x,y = queue.popleft()
                        for dx, dy in lists:
                            nx, ny = x + dx, y + dy

                            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0:
                                cnt += 1

                            elif grid[nx][ny] == 1:
                                queue.append((nx,ny))
                                grid[nx][ny] = 2


             
        return cnt
