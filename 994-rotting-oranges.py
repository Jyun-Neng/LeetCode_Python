"""
In a given grid, each cell can have one of three values:

    1. the value 0 representing an empty cell;
    2. the value 1 representing a fresh orange;
    3. the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.

Note:

    1. 1 <= grid.length <= 10
    2. 1 <= grid[0].length <= 10
    3. grid[i][j] is only 0, 1, or 2.

Example:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""
import collections


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        w = len(grid[0])
        h = len(grid)
        time = 0
        queue = collections.deque([])
        for x in range(w):
            for y in range(h):
                if grid[y][x] == 2:
                    queue.append([x, y, 0])
        while queue:
            x, y, time = queue.popleft()
            if x - 1 >= 0 and grid[y][x - 1] == 1:
                queue.append([x - 1, y, time + 1])
                grid[y][x - 1] = 2
            if x + 1 < w and grid[y][x + 1] == 1:
                queue.append([x + 1, y, time + 1])
                grid[y][x + 1] = 2
            if y - 1 >= 0 and grid[y - 1][x] == 1:
                queue.append([x, y - 1, time + 1])
                grid[y - 1][x] = 2
            if y + 1 < h and grid[y + 1][x] == 1:
                queue.append([x, y + 1, time + 1])
                grid[y + 1][x] = 2
        for x in range(w):
            for y in range(h):
                if grid[y][x] == 1:
                    return -1
        return time


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(Solution().orangesRotting(grid))
