"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    1. Integers in each row are sorted in ascending from left to right.
    2. Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        time complexity: O(M+N)
        """
        if not matrix:
            return False
        h = len(matrix)
        w = len(matrix[0])
        # start search from top-right
        x, y = w - 1, 0
        while x >= 0 and y < h:
            if target == matrix[y][x]:
                return True
            if target > matrix[y][x]:
                y += 1
            else:
                x -= 1
        return False


if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().searchMatrix(matrix, 5))
    print(Solution().searchMatrix(matrix, 20))
