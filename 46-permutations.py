"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def backtrack(self, start, end):
        if (start == end):
            self.res.append(self.nums[:])

        for i in range(start, end):
            # swap two numbers
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
            self.backtrack(start + 1, end)
            # restore the nums
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.res = []
        start = 0
        end = len(nums)
        self.backtrack(start, end)
        return self.res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
