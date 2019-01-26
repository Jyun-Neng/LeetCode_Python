"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example:

Input:
    11110
    11010
    11000
    00000
Output: 1
"""
import collections


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        queue = collections.deque([])
        h = len(grid)
        w = len(grid[0])
        cnt = 0
        for i in range(w):
            for j in range(h):
                if grid[j][i] == '1':
                    # replace '1' with '-' to represent visited land
                    grid[j][i] = '-'
                    queue.append([i, j])
                    cnt += 1
                    # BFS
                    while queue:
                        x, y = queue.popleft()
                        if x > 0 and grid[y][x - 1] == '1':
                            grid[y][x - 1] = '-'
                            queue.append([x - 1, y])
                        if x < w - 1 and grid[y][x + 1] == '1':
                            grid[y][x + 1] = '-'
                            queue.append([x + 1, y])
                        if y > 0 and grid[y - 1][x] == '1':
                            grid[y - 1][x] = '-'
                            queue.append([x, y - 1])
                        if y < h - 1 and grid[y + 1][x] == '1':
                            grid[y + 1][x] = '-'
                            queue.append([x, y + 1])
        return cnt


if __name__ == "__main__":
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(grid))
