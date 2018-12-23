'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
    """docstring for Solution"""
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        total_len = m + n

        if m >= n:
            b_len, s_len = m, n
            b_nums, s_nums = nums1, nums2
        else:
            b_len, s_len = n, m
            b_nums, s_nums = nums2, nums1 

        mid = total_len // 2
        first, last = 0, s_len 

        while first <= last:
            i = (first + last) // 2
            j = mid - i
            if i < s_len and b_nums[j-1] > s_nums[i]:
                # i is too small, must increase it
                first = i + 1 # may add to s_len
            elif i > 0 and s_nums[i-1] > b_nums[j]:
                # i is too big, must decrease it
                last = i
            else:
                # i is perfect
                if i == 0: max_left = b_nums[j-1]
                elif j == 0: max_left = s_nums[i-1]             # happen at s_len == b_len
                else: max_left = max(s_nums[i-1], b_nums[j-1])

                if i == s_len: min_right = b_nums[j]
                elif j == b_len: min_right = s_nums[i]          # happen at s_len == b_len
                else: min_right = min(s_nums[i], b_nums[j])

                return (max_left + min_right) / 2 if total_len % 2 == 0  else min_right

sol = Solution()
nums1 = [1]
nums2 = [3, 4]
mid = sol.findMedianSortedArrays(nums1, nums2)
print(mid)
