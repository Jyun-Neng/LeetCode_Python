"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        time complexity: O(log N)
        """
        if not matrix:
            return False
        h = len(matrix)
        w = len(matrix[0])
        l, r = 0, h * w - 1
        # see the 2D matrix as 1D array
        # binary search
        while l <= r:
            i = (l + r) >> 1
            x, y = i % w, i // w
            if target == matrix[y][x]:
                return True
            if target < matrix[y][x]:
                r = i - 1
            else:
                l = i + 1
        return False


if __name__ == "__main__":
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print(Solution().searchMatrix(matrix, target))
