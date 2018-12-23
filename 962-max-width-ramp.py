"""
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.
Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
"""
class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        time complexity: O(N)
        """
        max_num = -1
        for e in A:
            if max_num < e:
                max_num = e
        max_list = [-1 for x in range(0, max_num + 1)]
        min_list = [50001 for x in range(0, max_num + 1)]

        for i, e in enumerate(A):
            max_list[e] = max(max_list[e], i)
            min_list[e] = min(min_list[e], i)

        R = 0 
        width = 0
        for e in reversed(range(0, max_num + 1)):
            R = max(max_list[e], R)
            width = max(width, R - min_list[e])
        
        return width

if __name__ == "__main__":
    obj = Solution()
    A = [6,0,8,2,1,5]
    print(obj.maxWidthRamp(A))
