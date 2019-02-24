"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        n = len(nums)
        l, r = 0, n
        maxi = float('-inf')
        for i in range(n):
            if nums[i] > maxi:
                maxi = nums[i]
                p = i
        root = TreeNode(nums[p])
        root.left = self.constructMaximumBinaryTree(nums[l:p])
        root.right = self.constructMaximumBinaryTree(nums[p + 1:r])
        return root
