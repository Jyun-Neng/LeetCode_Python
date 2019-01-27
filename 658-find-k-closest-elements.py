"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
Note:

    1. The value k is positive and will always be smaller than the length of the sorted array.
    2. Length of the given array is positive and will not exceed 10^4
    3. Absolute value of elements in the array and x will not exceed 10^4

Example:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
"""


class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        time complexity: O(log(N-k))
        """
        l, r = 0, len(arr) - k
        # binary search
        while l < r:
            i = (l + r) >> 1
            # compare if the distance of left one or right one is closest to x
            # i is denoted the index of the smallest number in the closest elements list
            if x - arr[i] > arr[i + k] - x:
                l = i + 1   # i + 1 is the index of the smallest number in the closest elements list so far
            else:
                r = i   # i is the index of the smallest number in the closest elements list so far
        return arr[l:l + k]


if __name__ == "__main__":
    arr, k, x = [1, 2, 3, 4, 5], 4, 3
    print(Solution().findClosestElements(arr, k, x))
