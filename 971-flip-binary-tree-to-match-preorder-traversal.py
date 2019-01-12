"""
Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
A node in this binary tree can be flipped by swapping the left child and the right child of that node.
Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.
(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)
Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
If we cannot do so, then return the list [-1].

Input: root = [1,2], voyage = [2,1]
Output: [-1]
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    idx = 0
    # preorder traversal
    def dfs(self, node, nums, res):
        if not node:
            return True
        if node.val != nums[self.idx]:
            return False
        self.idx += 1
        if node.left and node.left.val != nums[self.idx]:
            if not node.right:
                return False
            res.append(node.val)
            # flip two sub trees
            return self.dfs(node.right, nums, res) and self.dfs(node.left, nums, res)
        return self.dfs(node.left, nums, res) and self.dfs(node.right, nums, res)

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        time complexity: O(N)
        """
        res = []
        if self.dfs(root, voyage, res):
            return res
        return [-1]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    nums = [1, 3, 2]
    print(Solution().flipMatchVoyage(root, nums))
