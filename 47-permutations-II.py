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
    def backtrack(self, tmp):
        if len(tmp) == self.size:
            self.res.append(tmp[:])
        for i in range(self.size):
            if self.visit[i]:
                continue
            # nums[i-1] and nums[i] are the same, so it does not require to add nums[i] to tmp again
            if i > 0 and self.nums[i] == self.nums[i - 1] and not self.visit[i - 1]:
                continue
            self.visit[i] = True    # nums[i] is added to tmp list
            tmp.append(self.nums[i])
            self.backtrack(tmp)
            tmp.pop()
            self.visit[i] = False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.size = len(nums)
        self.visit = [False for i in range(self.size)]
        self.nums = nums
        self.nums.sort()    # the same numbers are nearby
        self.res = []
        self.backtrack([])
        return self.res


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
