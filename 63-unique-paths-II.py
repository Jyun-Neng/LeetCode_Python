"""
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.
Now consider if some obstacles are added to the grids. How many unique paths would there be?
Note: m and n will be at most 100.

Example:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # there is a obstacle at start point
        if obstacleGrid[0][0] == 1:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        obstacle = False
        for x in range(w):
            if obstacleGrid[0][x] == 1 or obstacle:
                obstacleGrid[0][x] = 0
                obstacle = True
            else:
                obstacleGrid[0][x] = 1
        obstacle = False
        for y in range(1, h):
            if obstacleGrid[y][0] == 1 or obstacle:
                obstacleGrid[y][0] = 0
                obstacle = True
            else:
                obstacleGrid[y][0] = 1
        for y in range(1, h):
            for x in range(1, w):
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                else:
                    obstacleGrid[y][x] = obstacleGrid[y - 1][x] + \
                        obstacleGrid[y][x - 1]
        return obstacleGrid[-1][-1]


if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(Solution().uniquePathsWithObstacles(grid))
