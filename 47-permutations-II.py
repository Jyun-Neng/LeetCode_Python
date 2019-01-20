"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def backtrack(self, start, end):
        if (start == end):
            if self.nums not in self.res:
                self.res.append(self.nums[:])

        for i in range(start, end):
            if start != i and self.nums[start] == self.nums[i]:
                continue
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
            self.backtrack(start + 1, end)
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]

    def permuteUnique(self, nums):
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
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
