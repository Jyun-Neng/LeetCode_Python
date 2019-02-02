"""
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?
Note: m and n will be at most 100.

Example:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[m for x in range(m)] for y in range(n)]
        # first column
        for y in range(n):
            table[y][0] = 1
        # first row
        for x in range(m):
            table[0][x] = 1
        for y in range(1, n):
            for x in range(1, m):
                table[y][x] = table[y - 1][x] + table[y][x - 1]
        return table[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))
