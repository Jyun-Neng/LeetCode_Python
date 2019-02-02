"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        h, w = len(grid), len(grid[0])
        x = y = 0
        for y in range(h):
            for x in range(w):
                if x > 0 and y > 0:
                    if grid[y - 1][x] > grid[y][x - 1]:
                        grid[y][x] += grid[y][x - 1]
                    else:
                        grid[y][x] += grid[y - 1][x]
                else:
                    if x > 0:
                        grid[y][x] += grid[y][x - 1]
                    elif y > 0:
                        grid[y][x] += grid[y - 1][x]
        return grid[-1][-1]


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(grid))
