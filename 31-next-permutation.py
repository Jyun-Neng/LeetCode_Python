"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        time complexity: O(N)
        space complexity: O(1)
        """
        i = len(nums) - 2
        # find the first number (from right to left) that break the descending order
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        # find the next greater number greater than nums[i] between nums[i+1] to nums[-1] and swap them
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        # reverse sequence
        i += 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print(nums)
