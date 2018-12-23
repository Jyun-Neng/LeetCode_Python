"""
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.
If there isn't any rectangle, return 0.

Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
"""


class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        time complexity: O(N^4)
        """
        min_area = float('inf')
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    vec12 = [x2 - x1, y2 - y1]
                    vec13 = [x3 - x1, y3 - y1]
                    dot = vec12[0] * vec13[0] + vec12[1] * vec13[1]
                    if dot == 0:
                        x4, y4 = x2 + vec13[0], y2 + vec13[1]
                        if [x4, y4] in points:
                            area = ((vec12[0] ** 2 + vec12[1] ** 2) ** 0.5) * \
                                ((vec13[0] ** 2 + vec13[1] ** 2) ** 0.5)
                            min_area = min(min_area, area)
        return min_area if min_area < float('inf') else 0


if __name__ == "__main__":
    obj = Solution()
    points = [[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]
    print(obj.minAreaFreeRect(points))
