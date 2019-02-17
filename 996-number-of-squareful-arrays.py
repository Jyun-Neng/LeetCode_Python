"""
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, 
their sum is a perfect square. Return the number of permutations of A that are squareful.
Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

Note:

    1.1 <= A.length <= 12
    2. 0 <= A[i] <= 1e9

Example:

Input: [1,17,8]
Output: 2
Explanation:
[1,8,17] and [17,8,1] are the valid permutations.
"""
import collections


class Solution(object):
    def backtrack(self, i, N):
        self.cnt[i] -= 1
        if N == 0:
            self.res += 1
        for j in self.table[i]:
            if self.cnt[j]:
                self.backtrack(j, N - 1)
        self.cnt[i] += 1

    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.res = 0
        N = len(A) - 1
        self.cnt = collections.Counter(A)
        self.table = collections.defaultdict(list)
        for i in self.cnt:
            self.table[i] = [j for j in self.cnt if int(
                (i + j)**0.5)**2 == i + j]
        # find all permutations
        for i in self.cnt:
            self.backtrack(i, N)
        return self.res


if __name__ == "__main__":
    print(Solution().numSquarefulPerms([1, 17, 8]))
