"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def search(self, node):
        if not node:
            return
        self.search(node.left)
        self.k -= 1
        if self.k == 0:
            self.ans = node.val
            return
        self.search(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.ans = None
        self.search(root)
        return self.ans


if __name__ == "__main__":
    vals = [3, 1, 4, None, 2]
    root = TreeNode(vals[0])
    node = root
    node.left = TreeNode(vals[1])
    node.right = TreeNode(vals[2])
    node = node.left
    node.right = TreeNode(vals[4])
    print(Solution().kthSmallest(root, 1))
