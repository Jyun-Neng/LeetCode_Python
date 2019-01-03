"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Input: [1,1,1,1,1,null,1]
Output: true
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node, vals):
        if node:
            vals.append(node.val)
            self.dfs(node.left, vals)
            self.dfs(node.right, vals)

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        time complexity: O(N)
        """
        vals = []
        self.dfs(root, vals)
        return len(set(vals)) == 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    left = root.left
    left.left = TreeNode(1)
    print(Solution().isUnivalTree(root))
