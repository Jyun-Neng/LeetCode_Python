"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.
Note:

    1. You must not modify the array (assume the array is read only).
    2. You must use only constant, O(1) extra space.
    3. Your runtime complexity should be less than O(n2).
    4. There is only one duplicate number in the array, but it could be repeated more than once.

Example:

Input: [1,3,4,2,2]
Output: 2
"""


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        time complexity: O(N)
        space complexity: O(1)
        """
        slow, fast = nums[0], nums[0]
        # detect loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # find duplicate number
        num1, num2 = nums[0], slow
        while num1 != num2:
            num1 = nums[num1]
            num2 = nums[num2]

        return num1


if __name__ == "__main__":
    nums = [3, 1, 3, 4, 2]
    print(Solution().findDuplicate(nums))
