"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
The intersection of two closed intervals is a set of real numbers that is either empty, 
or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        i = j = 0
        ans = []
        while i < len(A) and j < len(B):
            lo, hi = max(A[i].start, B[j].start), min(A[i].end, B[j].end)
            if lo <= hi:
                ans.append(Interval(lo, hi))
            # find the smallest endpoint between A[i] and B[j]
            # and increase the index
            # because it cannot intersect anything else
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1
        return ans


if __name__ == "__main__":
    a = [[0, 2], [5, 10], [13, 23], [24, 25]]
    b = [[1, 5], [8, 12], [15, 24], [25, 26]]
    A = []
    B = []
    for s, e in a:
        A.append(Interval(s, e))
    for s, e in b:
        B.append(Interval(s, e))

    ans = Solution().intervalIntersection(A, B)
    for a in ans:
        print(a.start, a.end)
